# Create new thread that pulls from central data and checks if can execute open order
# every x seconds
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

import heapq
import traceback
from prototrade.models.dual_heap import DualHeap
from prototrade.exceptions.exceptions import InvalidOrderTypeException, InvalidOrderSideException, UnknownOrderIdException, MissingParameterException, ExtraneousParameterException, UnavailableSymbolException, InvalidPriceException, InvalidVolumeException
from prototrade.models.order import Order
import math
from threading import Thread
from copy import deepcopy
from prototrade.models.transaction import Transaction
import time
from collections import defaultdict
from threading import Lock
import datetime
import numpy as np
import csv
from prototrade.models.error_event import ErrorEvent
from prototrade.models.enums import OrderType, OrderSide

SYMBOL_REQUEST_TIMEOUT = 12

DATETIME_FORMAT = "%y-%m-%d %H:%M:%S"
class PositionManager:
    def __init__(self, order_books_dict, order_books_dict_semaphore, stop_event, error_queue, exchange_num, subscribed_symbols, save_data_location, file_locks):
        self._order_books_dict = order_books_dict
        self._order_books_dict_semaphore = order_books_dict_semaphore
        self._stop_event = stop_event
        self._error_queue = error_queue
        self._exchange_num = exchange_num
        self._subscribed_symbols = subscribed_symbols
        self._save_data_location = save_data_location
        self._file_locks = file_locks

        logger.debug(f"Strategy saving at {self._save_data_location}")

        self._open_orders_polling_thread = None
        self._positions_map = defaultdict(int)
        self._open_orders = dict() # symbol name -> (bid heap, ask heap)
        self._transaction_history = []
        self._order_dict = dict() # order_id -> heap object
        self._largest_order_id = -1 #Initally no orders placed
        self._transaction_pnl = 0

        self._open_orders_polling_thread = None

        self.initialise_locks()
        self.initialise_file_pointers()
        
    def initialise_locks(self):
        self._order_objects_lock = Lock() # have to acquire lock whenever accessing order_dict or open_orders
        self._positions_map_lock = Lock()
        self._transaction_pnl_lock = Lock()
        self._transaction_history_lock = Lock()

    def initialise_file_pointers(self):
        self.pnl_file = open(self._save_data_location/"PnL.csv", "a+")
        self.csv_writer_pnl = csv.writer(self.pnl_file)
        self.csv_reader_pnl = csv.reader(self.pnl_file, delimiter=',')

        self.transactions_file = open(self._save_data_location/"Transactions.csv", "a+")
        self.csv_writer_transactions = csv.writer(self.transactions_file)
        self.csv_reader_transactions = csv.reader(self.transactions_file, delimiter=',')
        
        self.positions_file = open(self._save_data_location/"Positions.csv", "a+")
        self.csv_writer_positions = csv.writer(self.positions_file)
        self.csv_reader_positions = csv.reader(self.positions_file, delimiter=',')
        

    def create_order(self, symbol, order_side, order_type, volume, price = None):
        # FOC: check if order can be executed immediately (don't add to open orders)
        # Limit: add order with limit price to open orders
        # Market: add order with inf bid price / 0 ask price
        if not self._open_orders_polling_thread:
            self._create_thread_to_poll_open_orders() #Start thread to poll open orders

        self._order_objects_lock.acquire()
        if symbol not in self._open_orders:
            # Create dual heap if this is the 1st order
            self._open_orders[symbol] = DualHeap()
            logger.debug(f"Creating heap for {symbol}")

        dual_heap = self._open_orders[symbol]
        
        if price and not np.isreal(price):
            self.release_locks()
            raise TypeError(f"The price parameter given, {price}, must be an integer or float. {type(price)}")

        if not isinstance(volume,(int, np.integer)):
            self.release_locks()
            raise TypeError(f"The volume parameter given, {volume}, must be an integer.")

        if volume <= 0:
            raise InvalidVolumeException("Order volume must be greater than zero")

        if price and price < 0:
            raise InvalidPriceException("Order price must be zero or greater")

        if order_side == OrderSide.BID:
            heap_to_use = dual_heap.bid_heap
        elif order_side == OrderSide.ASK:
            heap_to_use = dual_heap.ask_heap
        else:
            self.release_locks()
            raise InvalidOrderSideException(f"'{order_side}' is an invalid order side. Valid order sides: OrderSide.BID, OrderSide.ASK")

        if order_type in [OrderType.LIMIT, OrderType.FOK] and not price:
            self.release_locks()
            raise MissingParameterException(f"Must include price as a parameter when inserting a {order_type} order in create_order")

        elif order_type == OrderType.MARKET and price:
            self.release_locks()
            raise ExtraneousParameterException("Price cannot be used as parameter when a market order type is specified in create_order")
            
        if symbol not in self._subscribed_symbols: # needs live data for symbol as otherwise cannot simulate execution 
            raise UnavailableSymbolException(f"Subscribe to symbol '{symbol}' before creating an order for '{symbol}'")

        if order_type == OrderType.FOK:
            self.release_locks() # fok doesn't use heap so can release lock
            return self._handle_fok(symbol, order_side, volume, price)
        elif order_type == OrderType.LIMIT:
            return self._handle_limit_order(heap_to_use, symbol, order_side, order_type, volume, price)
        elif order_type == OrderType.MARKET:
            return self._handle_market_order(heap_to_use, symbol, order_side, order_type, volume)
        else:
            self.release_locks()
            raise InvalidOrderTypeException(f"'{order_type}' is an invalid order type. Valid order types: OrderType.MARKET, OrderType.LIMIT, OrderType.FOK")

        # Need to add the order to dual heap, then add a entry in the _order_dict to that new object
        # As the key for the entry, create a new order_id
        # return newly created order_id

    def _insert_order(self, heap_to_use, symbol, order_side, order_type, volume, price):
        order_id = self._get_next_order_id()
        order = Order(order_id, symbol, order_side, order_type, volume, price)
        heapq.heappush(heap_to_use, order)
        self._order_dict[order_id] = order
        self._order_objects_lock.release()
        logger.debug(f"Order with order_id {order_id} inserted")

        return order_id

    def _handle_fok(self, symbol, order_side, volume, price):
        self._order_books_dict_semaphore.acquire()

        if symbol not in self._order_books_dict:
            self._wait_for_symbol_to_arrive(symbol)

        quote_for_symbol = deepcopy(self._order_books_dict[symbol]) # get a copy of the current prices
        self._order_books_dict_semaphore.release()
        if order_side == OrderSide.BID:
            best_ask_half_quote = quote_for_symbol.ask #match strategy bid against real ask
            if price >= best_ask_half_quote.price:
                return self._register_new_transaction(symbol, order_side, OrderType.FOK, volume, best_ask_half_quote.price, time.time())
        else:
            best_bid_half_quote = quote_for_symbol.bid #match strategy bid against real ask
            if price <= best_bid_half_quote.price:
                return self._register_new_transaction(symbol, order_side, OrderType.FOK, volume, best_bid_half_quote.price, time.time())
        
        self.write_positions_to_csv()
        return None # None if FOK order was killed

    def _handle_limit_order(self, heap_to_use, symbol, order_side, order_type, volume, price):
        return self._insert_order(heap_to_use, symbol, order_side, order_type, volume, price)

    def _handle_market_order(self, heap_to_use, symbol, order_side, order_type, volume):
        if order_side == OrderSide.BID:
            return self._insert_order(heap_to_use, symbol, order_side, order_type, volume, math.inf)
        else:
            return self._insert_order(heap_to_use, symbol, order_side, order_type, volume, 0)


    def _wait_for_symbol_to_arrive(self, symbol):
        if symbol not in self._subscribed_symbols:
            self._order_books_dict_semaphore.release()
            self.release_locks()
            raise UnavailableSymbolException(f"In strategy {self._exchange_num} requesting live data on symbol '{symbol}', but strategy is not subscribed to '{symbol}'")
        
        start_time = time.time()
        while symbol not in self._order_books_dict:
            self._order_books_dict_semaphore.release()
            time.sleep(0.2)
            logger.debug(f"PM Waiting for {symbol} to come in")
            self._order_books_dict_semaphore.acquire()

            if time.time() - start_time > SYMBOL_REQUEST_TIMEOUT:
                self._order_books_dict_semaphore.release()
                self.release_locks()
                raise UnavailableSymbolException(
                    f"Symbol request timeout: strategy number {self._exchange_num} cannot find requested symbol '{symbol}' from exchange. Check symbol exists & exchange is open.")

            if self._stop_event.is_set():
                self._order_books_dict_semaphore.release()
                self.release_locks()
                raise UnavailableSymbolException(
                    f"Interrupt while waiting for symbol '{symbol}' to arrive in strategy number {self._exchange_num}")

    def cancel_order(self, order_id, volume_requested = None):
        # remove volume from order
        # if volume_requested > order_volume -> remove entire order
        if type(order_id) != int:
            raise TypeError(f"The order_id parameter given, {order_id}, must be an integer.")

        if volume_requested and type(volume_requested) != int:
            raise TypeError(f"The volume_requested parameter given, {volume_requested}, must be an integer.")

        self._order_objects_lock.acquire()
        if order_id not in self._order_dict:
            self.release_locks()
            raise UnknownOrderIdException(f"Order ID {order_id} unknown")
        
        order = self._order_dict[order_id]
        dual_heap = self._open_orders[order.symbol]

        if order.order_side == OrderSide.BID:
            heap_to_use = dual_heap.bid_heap
        else:
            heap_to_use = dual_heap.ask_heap

        if not volume_requested or volume_requested >= order.volume:
            self._remove_from_heap(heap_to_use, order) #Remove from heap
            del self._order_dict[order_id] #Remove from order dict
            logger.debug(f"{order_id} deleted")
        else:
            order.volume -= volume_requested
        
        self._order_objects_lock.release()

    def _remove_from_heap(self, heap_to_use, order):
        # Remove order from heap and re-heapify
        heap_to_use.remove(order)
        heapq.heapify(heap_to_use)

    def get_orders(self, symbol = None):
        # dictionary of order_id -> Order Object

        self._order_objects_lock.acquire()
        if symbol:
            # Only return orders for requested symbol
            ret = {k:v for k,v in self._order_dict.items() if v.symbol == symbol} 
        else:
            ret = deepcopy(self._order_dict)

        self._order_objects_lock.release()
        return ret 

    # Next order ID to assign
    def _get_next_order_id(self):
        self._largest_order_id += 1
        return self._largest_order_id

    def _get_heap(self, symbol):
        self._order_objects_lock.acquire()
        heap = str(self._open_orders[symbol])
        self._order_objects_lock.release()
        return heap

    def get_strategy_best_bid(self, symbol):
        self._order_objects_lock.acquire()
        if symbol not in self._open_orders:
            self._order_objects_lock.release()
            return None #If no orders ever placed, we can just return None

        bid_heap = self._open_orders[symbol].bid_heap
        if bid_heap:
            best_bid = deepcopy(bid_heap[0])
        else:
            best_bid = None

        self._order_objects_lock.release()
        return best_bid

    def get_strategy_best_ask(self, symbol):
        self._order_objects_lock.acquire()
        if symbol not in self._open_orders:
            self._order_objects_lock.release()
            return None #If no orders ever placed, we can just return None

        ask_heap = self._open_orders[symbol].ask_heap
        if ask_heap:
            best_ask = deepcopy(ask_heap[0])
        else:
            best_ask = None

        self._order_objects_lock.release()
        return best_ask

    def _create_thread_to_poll_open_orders(self):
        self._open_orders_polling_thread = Thread(
            target=self._start_thread)  
        self._open_orders_polling_thread.start()

    def _start_thread(self):
        try:
            self._check_for_executable_orders()
        except Exception as e: # if exception in thread then release all locks and place error on queue       
            self.release_locks()
            handle_error(self._error_queue, self._exchange_num)
       
    def release_locks(self):
        logger.debug("Closing files")
        if self.pnl_file:
            self.pnl_file.close()
        if self.transactions_file:
            self.transactions_file.close()

        logger.debug("Releasing all PM locks")
        if self._order_objects_lock.locked():
            self._order_objects_lock.release()
        
        if self._positions_map_lock.locked():
            self._positions_map_lock.release()
        
        if self._transaction_pnl_lock.locked():
            self._transaction_pnl_lock.release
        
        if self._transaction_history_lock.locked():
            self._transaction_history_lock.release()

    def _check_for_executable_orders(self):
        logger.debug("Starting open order polling thread")
        last_log_time = time.time()
        while not self._stop_event.is_set():
            self._order_books_dict_semaphore.acquire()
            for symbol in self._open_orders:
                if symbol not in self._order_books_dict: 
                    self._wait_for_symbol_to_arrive(symbol) 
            order_books_snapshot = deepcopy(self._order_books_dict) # get a copy of the current prices
            self._order_books_dict_semaphore.release()

            self._order_objects_lock.acquire()
            for symbol, dual_heap in self._open_orders.items(): # look through every symbol's dual heap 
                symbol_quote = order_books_snapshot[symbol]
                self.execute_any_bid_orders(symbol, dual_heap.bid_heap, symbol_quote.ask)
                self.execute_any_ask_orders(symbol, dual_heap.ask_heap, symbol_quote.bid)
            self._order_objects_lock.release()

            if time.time() - last_log_time > 1:
                self.write_pnl_to_csv()
                last_log_time = time.time()

            time.sleep(0.3)
  
        logger.debug("Open order polling thread finished")

    def write_positions_to_csv(self):
        timestamp = datetime.datetime.now().strftime(DATETIME_FORMAT)
        
        self._positions_map_lock.acquire()
        positions = deepcopy(self._positions_map)
        self._positions_map_lock.release()

        self._file_locks.positions_lock.acquire()
        for k, v in positions.items():
            self.csv_writer_positions.writerow([timestamp, k, v])

        self.positions_file.flush() # flush data to file
        self._file_locks.positions_lock.release()

    def _get_timestamp(self):
        return datetime.datetime.now().strftime(DATETIME_FORMAT)

    def write_pnl_to_csv(self):
        timestamp = self._get_timestamp()
        self._file_locks.pnl_lock.acquire()
        pnl = round(self.get_pnl(), 3)
        self.csv_writer_pnl.writerow([timestamp, pnl])
        self.pnl_file.flush() # flush data to file
        self._file_locks.pnl_lock.release()

    def get_pnl_over_time(self):
        self._file_locks.pnl_lock.acquire()
        self.pnl_file.seek(0) # seek to start of file to read all
        
        pnl_list = list(self.csv_reader_pnl)

        if len(pnl_list) == 0:
            self._file_locks.pnl_lock.release()
            return None
        
        self._file_locks.pnl_lock.release()

        for pair in pnl_list:
            pair[0] = datetime.datetime.strptime(pair[0], DATETIME_FORMAT)
            pair[1] = float(pair[1])
        
        return pnl_list

    def get_positions_over_time(self, symbol_filter = None):
        positions = []

        self._file_locks.positions_lock.acquire()
        self.positions_file.seek(0)

        if symbol_filter:
            for row in self.csv_reader_positions:
                logger.debug(row)
                if row[1] == symbol_filter: 
                    positions.append(row)
        else:
            positions = list(self.csv_reader_positions)

        for l in positions:
            l[0] = datetime.datetime.strptime(l[0], DATETIME_FORMAT)
            l[2] = int(l[2])

        self._file_locks.positions_lock.release()
        return positions

    def _register_new_transaction(self, symbol, order_side, order_type, volume, price, time):
        t = Transaction(symbol, order_side, order_type, volume, price, time)
        self._transaction_history_lock.acquire()
        self.csv_writer_transactions.writerow([t.symbol, t.order_side, t.order_type, t.volume, t.price, t.timestamp])
        self._transaction_history_lock.release()
        self._positions_map_lock.acquire()
        if order_side == OrderSide.BID:
            self._positions_map[symbol] += volume
        else:
            self._positions_map[symbol] -= volume
        self._positions_map_lock.release()

        transaction_amount = t.price * t.volume

        self._transaction_pnl_lock.acquire()
        if t.order_side == OrderSide.BID:
            self._transaction_pnl -= transaction_amount # bid side so lost money and gained assets
        else:
            self._transaction_pnl += transaction_amount # ask side so gained money and lost assets

        self._transaction_pnl_lock.release()
        return t

    def execute_any_bid_orders(self, symbol, bid_heap, live_best_ask_half_quote):
        executed = None
        while bid_heap and bid_heap[0].price >= live_best_ask_half_quote.price:
            executed = heapq.heappop(bid_heap)
            logger.debug(f"EXECUTED bid order at price {live_best_ask_half_quote.price}: {executed}")

            self._register_new_transaction(symbol, executed.order_side, executed.order_type, executed.volume, live_best_ask_half_quote.price, time.time())
            del self._order_dict[executed.order_id]
        
        if executed:
            self.write_positions_to_csv()

    def execute_any_ask_orders(self, symbol, ask_heap, live_best_bid_half_quote):
        executed = None
        while ask_heap and ask_heap[0].price <= live_best_bid_half_quote.price:
            executed = heapq.heappop(ask_heap)
            logger.debug(f"EXECUTED ask order at price {live_best_bid_half_quote.price}: {executed}")
            
            self._register_new_transaction(symbol, executed.order_side, executed.order_type, executed.volume, live_best_bid_half_quote.price, time.time())
            del self._order_dict[executed.order_id]
        if executed:
            self.write_positions_to_csv()

    def get_positions(self, symbol_filter = None):
        self._positions_map_lock.acquire()
        if symbol_filter:
            pos = self._positions_map[symbol_filter] # int of positions
        else:
            pos = deepcopy(self._positions_map)
        self._positions_map_lock.release()
        return pos

    def get_transactions(self, symbol_filter = None):
        self._transaction_history_lock.acquire()
        self.transactions_file.seek(0) # seek to start of file to read all
        trans = []
        
        if symbol_filter:
            for row in self.csv_reader_transactions:
                if row[0] ==  symbol_filter:
                    trans.append(Transaction(*row))
        else:
            for row in self.csv_reader_transactions:
                trans.append(Transaction(*row))
        self._transaction_history_lock.release()
        return trans

    def get_realised_pnl(self):
        self._transaction_pnl_lock.acquire()
        val = self._transaction_pnl
        self._transaction_pnl_lock.release()
        return val

    def get_pnl(self):
        # for each transaction: price * -volume if bid (lost money gained assets). price * volume if ask (gained money lost assets)
        # for each current position: if position_vol > 0: best_ask * position_vol, if position_vol < 0: best_bid * position_vol
        
        pnl = self._transaction_pnl # pnl acquired by the transaction history
        # atomic so doesn't need a lock

        self._positions_map_lock.acquire()
        positions = deepcopy(self._positions_map)
        self._positions_map_lock.release()

        self._order_books_dict_semaphore.acquire()
        for symbol in self._positions_map:
            if symbol not in self._order_books_dict:
                self._wait_for_symbol_to_arrive(symbol)
        order_books_snapshot = deepcopy(self._order_books_dict) # get a copy of the current prices

        self._order_books_dict_semaphore.release()

        # add all unrealised pnl from current positions
        
        for symbol, amount in positions.items():
            if amount > 0:
                pnl += order_books_snapshot[symbol].bid.price * amount # the money obtained if all shares were sold at best bid price
            elif amount < 0:
                pnl += order_books_snapshot[symbol].ask.price * amount # the money spent to obtain all shares back at best ask price

        return pnl

    def hack_out(self):
        self._order_objects_lock.acquire()
        for order_id in self._order_dict:
            self.cancel_order(order_id)
        self._order_objects_lock.release()
    
# Thread that pseudo-executes orders must give a transaction price of the corresponding bid/ask price, not the limit price 
# MATCHING ORDERS AGAINST OWN ORDERS?

def handle_error(error_queue, exchange_num):
    exception_info = traceback.format_exc() # Get a string with full original stack trace
    error_queue.put(ErrorEvent(exchange_num, exception_info))
    logger.error(f"Process PM {exchange_num} EXCEPTION")