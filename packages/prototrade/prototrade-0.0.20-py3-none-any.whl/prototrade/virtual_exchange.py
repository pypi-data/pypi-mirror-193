


import multiprocessing
from multiprocessing import Manager, Pool
from multiprocessing.managers import BaseManager, NamespaceProxy
from prototrade.ticker_streamer.alpaca_streamer import AlpacaDataStreamer
from prototrade.ticker_streamer.price_updater import PriceUpdater
from prototrade.models.strategy import Strategy
from prototrade.exchange.exchange import Exchange
from prototrade.ticker_streamer.subscription_manager import SubscriptionManager
from prototrade.exceptions.error_processor import ErrorProcessor
from prototrade.models.error_event import ErrorEvent
from prototrade.exceptions.exceptions import ExchangeNotOpenException
from pathlib import Path

import traceback
import signal
import logging

TEST_SYMBOLS = ["AAPL", "GOOG", "MSFT"]

SENTINEL = None

logging.basicConfig(level=logging.INFO)

class VirtualExchange:
    """The master class used for initialising & running the framework. Handles allocating processes to each of the registered strategies.

    :raises ExchangeNotOpenException: If the exchange is currently closed, this error is raised
    """

    # this should be initialised with alpaca credentials and exchange. then register_strategy sued to calculate the num_strategiegs
    def __init__(self, streamer_name, streamer_username, streamer_key, exchange_name="iex", save_data_location = None):
        """_summary_

        :param streamer_name: The name of the streamer to use. Recommended: ``'alpaca'``
        :type streamer_name: str
        :param streamer_username: The API usesrname
        :type streamer_username: str
        :param streamer_key: The corresponding API key
        :type streamer_key: str
        :param exchange_name: The exchange to use. For alpaca, this can be ``sip`` (all US exchanges - paid subscription only) or ``iex``, defaults to "iex"
        :type exchange_name: str, optional
        :param save_data_location: The relative file location (from the user strategy script) to save data about each run, defaults to None
        :type save_data_location: str, optional
        """
        
        signal.signal(signal.SIGINT, self._exit_handler)
        self._streamer_name = streamer_name
        self._streamer_username = streamer_username
        self._streamer_key = streamer_key
        self._exchange_name = exchange_name

        if not save_data_location:
            self.save_data_location =  Path('.')

        self._pre_setup_terminate = False
        self._setup_finished = False

        self._streamer = None
        self._stop_event = None
        self._strategy_process_pool = None
        self._rest_api_manager = None
        self._subscription_manager = None
        self._subscription_queue = None
        self._error_queue = None
        self._error_processor = None

        self.num_strategies = 0  # This will be incremented when strategies are added
        self._strategy_list = []

    def _create_processes_for_strategies(self):
        logging.info(f"Number of strategies: {self.num_strategies}")

        # Temporarily ignore SIGINT to prevent interrupts being handled in child processes
        signal.signal(signal.SIGINT, signal.SIG_IGN)

        # SIGINT ignored to set child processes so wrap pool creation in a try except

        # Windows only supports spawning processes (instead of forking), so design design has been taking to always spawn regardless of operating system
        try:
            self._strategy_process_pool = multiprocessing.get_context('spawn').Pool(
                self.num_strategies)  # USE SPAWN HERE? Check bloat
        except KeyboardInterrupt:
            self._stop()

        # Set the handler for SIGINT. Now SIGINT is only handled in the main process
        signal.signal(signal.SIGINT, self._exit_handler)

        logging.info("Creating strategy processes")
        
        for strategy_num, strategy in enumerate(self._strategy_list):
            exchange = Exchange(
                self._order_books_dict, self._order_books_dict_semaphore, self._subscription_queue, self._error_queue, strategy_num, self._stop_event, self._historical_api, self.save_data_location)
            logging.info("TEST")
            res = self._strategy_process_pool.apply_async(
                _run_strategy, args=(self._error_queue, strategy.strategy_func, exchange, *strategy.arguments))
            logging.info(f"Started strategy {strategy_num}")

        logging.info("Started strategies")
        self._error_processor._join_thread()
        logging.info("Error processing thread joined")

        self._stop()

    def _stop(self, should_exit=True):
        logging.info("Stopping Program")
        self._stop_event.set()  # Inform child processes to stop
        # logging.info(self._error_processor.exception)
        # Prevents any other task from being submitted
        if self._strategy_process_pool:  # Only close pool if it was opened
            logging.info("Joining processes")
            self._strategy_process_pool.close()
            self._strategy_process_pool.join()  # Wait for child processes to finish
            logging.info("Processes terminated")

        if self._subscription_manager:
            self._subscription_manager.stop_queue_polling()
            logging.info("Subscription manager stopped")

        # Clean up processes before the streamer as processes rely on streamer
        if self._rest_api_manager:
            self._rest_api_manager.shutdown()

        if self._streamer:
            self._streamer.stop()
            logging.info("Streamer stopped")

        if self._error_processor:
            if self._error_processor.is_error:
                logging.info(self._error_processor.exception)
            else:
                self._error_processor._stop_queue_polling()
            logging.info("Error processor stopped")

        if should_exit:
            logging.info("Exiting")
            exit(0)  # All user work done so can exit
        logging.info("No exit in stop()")

    def _create_shared_memory(self, num_readers):
        self.manager = Manager()
        shared_dict = self.manager.dict()
        self._order_books_dict_semaphore = self.manager.Semaphore(num_readers)
        self._stop_event = self.manager.Event()

        return shared_dict

    def _exit_handler(self, signum, _):
        if signum == signal.SIGINT:
            logging.info("\nStopping...")
            if self._setup_finished:
                self._stop()
            else:
                self._pre_setup_terminate = True

    def register_strategy(self, strategy_func, *args):
        """Register a function to be executed. Include any arguments that the strategy function should be provided. N.B. When the strategies are started, each strategy function
        is always provided with an `Exchange <prototrade.exchange.exchange.Exchange>` object as the first parameter. This enables the strategy to interact with the framework.

        :param strategy_func: A strategy function to register
        :type strategy_func: function
        :param args: the parameters to pass to the strategy function, optional
        :type args: any
        """
        self.num_strategies += 1
        self._strategy_list.append(Strategy(strategy_func, args))

    def run_strategies(self):
        """
        Begins the execution of all strategies
        """
        try:
            self._create_components() # Try to start all the components and user strategies
        except Exception as e:
            self._stop(False)  # Cleanup then re-raise exception
            raise (e)

    def _create_components(self):
        self._order_books_dict = self._create_shared_memory(
            self.num_strategies)

        self.price_updater = PriceUpdater(
            self._order_books_dict, self._order_books_dict_semaphore, self.num_strategies, self._stop_event)

        self._streamer = AlpacaDataStreamer(
            self._streamer_username,
            self._streamer_key,
            self.price_updater,
            self._exchange_name
        )

        if not self._streamer.is_market_open():
            raise ExchangeNotOpenException(
                f"The live exchange is currently closed. Try again during trading hours")

        self._create_shared_rest_api_class()

        self._subscription_queue = self.manager.Queue()

        self._subscription_manager = SubscriptionManager(self._streamer,
                                                         self._subscription_queue, SENTINEL)

        self._error_queue = self.manager.Queue()

        self._error_processor = ErrorProcessor(self._error_queue, SENTINEL)

        logging.info("Creating streamer")

        self._setup_finished = True
        if self._pre_setup_terminate:
            self._stop()  # If CTRL-C pressed while setting up, then trigger stop now

        self._create_processes_for_strategies()

    # This creates a REST api object that is shareable across strategy processes. This means the user can query historical data
    def _create_shared_rest_api_class(self):
        _CustomManager.register(
            'HistoricalAPI', _HistoricalAPI, _HistoricalAPIProxy)
        self._rest_api_manager = _CustomManager()
        self._rest_api_manager.start()
        rest_api = self._rest_api_manager.HistoricalAPI(
            self._streamer.get_rest_api())  # Pass in the actual rest api as a parameter
        # Get the api object within the class wrapper
        self._historical_api = rest_api.api

# This has to be outside the class, as otherwise all class members would have to be pickled when sending arguments to the new process


def _run_strategy(error_queue, func, exchange, *args):
    try:  # Wrap the user strategy in a try/catch block so we can catch any errors and forward them to the main process
        logging.info(f"Running {exchange.exchange_num}")
        func(exchange, *args)
    except Exception:
        try:
            _handle_error(error_queue, exchange.exchange_num)
        except Exception as e2:
            logging.critical(
                f"During handling of a strategy error, another error occured: {e2}")
        # At this point the process has finished and can be joined with the main process


def _handle_error(error_queue, exchange_num):
    logging.error(f"Process {exchange_num} EXCEPTION")
    # Get a string with full original stack trace
    exception_info = traceback.format_exc()
    error_queue.put(ErrorEvent(exchange_num, exception_info))


class _CustomManager(BaseManager):
    pass


class _HistoricalAPI:
    def __init__(self, api):
        self.api = api  # Holds the api to be used to acquire historical data


class _HistoricalAPIProxy(NamespaceProxy):
    # We need to expose the same __dunder__ methods as NamespaceProxy,
    # in addition to the b method.
    _exposed_ = ('__getattribute__', '__setattr__', '__delattr__', 'api')

