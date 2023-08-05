from prototrade.virtual_exchange import VirtualExchange
import time
import random
from matplotlib import pyplot as plt
import pandas as pd


def main():
    pt = VirtualExchange("alpaca",
                    "AKFA6O7FWKEQ30SFPB9H",
                    "z6Cb3RW4lyp3ykub09tUHjdGF7aNYsGuqXh7WWJs",
                    "sip")
    pt.register_strategy(test_strategy, 5, 8)
    pt.run_strategies()

# Boilerplate strategy that retrieves the price of Apple stock and places a market order every 3 seconds
# Example parameters to to specify the arguments for the random.randrange function in the market order
def test_strategy(exchange, lower_volume, upper_volume):
    print(f"Lower volume:{lower_volume} p2:{upper_volume}")

    exchange.subscribe("AAPL") # Subscribe to live data from Apple
    while exchange.is_running():
        order_books = exchange.get_subscribed_books()
        aapl_price = order_books["AAPL"]
        print(f"AAPL BID PRICE: {aapl_price.bid}")
        print(f"AAPL ASK PRICE: {aapl_price.ask}")
        
        exchange.create_order("AAPL", "bid", "market", random.randrange(lower_volume, upper_volume)) # Example of placing an order with random volume within the limits

        for x in exchange.get_orders("AAPL").items():
            print(x)
        
        print("Transactions:", exchange.get_transactions())
        print("Positions", exchange.get_positions())

        pnl_pd = pd.DataFrame(exchange.get_pnl_over_time(), columns = ['timestamp', 'pnl'])
        if not pnl_pd.empty:
            plot = pnl_pd.plot(x="timestamp", y="pnl")
            plot.set_xlabel("TimeStamp")
            plot.set_ylabel("Profit / Loss")
            plt.savefig("test2")

        print("---------------")
        time.sleep(3)
        
    print("Strategy 0 FINISHED")

if __name__ == '__main__': 
    main()
