# File with some binance functions
# See: https://python-binance.readthedocs.io/en/latest/market_data.html
# https://python-binance.readthedocs.io/en/latest/binance.html

import config
from binance.client import Client

client = Client(config.API_KEY, config.API_SECRET)

# # get binance server time
# time_res = client.get_server_time()
# print(time_res)

# # Get all ticker prices
# prices = client.get_all_tickers()
# print(prices)

# # Get historical data of coin and create csv
# csvfile = open("btc_1day.csv", "w", newline="")
# candlestick_writer = csv.writer(csvfile, delimiter=",")

# candlesticks = klines = client.get_historical_klines(
#     "BTCUSDT", Client.KLINE_INTERVAL_1DAY, "1 Jan, 2020", "20 Sept, 2020"
# )

# for candle in candlesticks:
#     candle[0] = candle[0] / 1000
#     print(candle, candle[0])
#     candlestick_writer.writerow(candle)

# # Get system status
# status = client.get_system_status()
# print(status)

# Get Exchange Info like rate limits!
# info = client.get_exchange_info()
# print(info)

# Get the exchange info for a particular symbol
# info = client.get_symbol_info("BNBBTC")
# print(info)

# # Get Market Depth
# depth = client.get_order_book(symbol="BNBBTC")
# print(depth)

# # Get Recent Trades
# trades = client.get_recent_trades(symbol="BNBBTC")
# print(trades)

# Fetch klines for any date range and interval

# # fetch 1 minute klines for the last day up until now
# klines = client.get_historical_klines("BNBBTC", Client.KLINE_INTERVAL_1MINUTE, "1 day ago UTC")

# # fetch 30 minute klines for the last month of 2017
# klines = client.get_historical_klines("ETHBTC", Client.KLINE_INTERVAL_30MINUTE, "1 Dec, 2017", "1 Jan, 2018")

# # fetch weekly klines since it listed
# klines = client.get_historical_klines("NEOBTC", Client.KLINE_INTERVAL_1WEEK, "1 Jan, 2017")

# Fetch klines using a generator

# for kline in client.get_historical_klines_generator(
#     "BNBBTC", Client.KLINE_INTERVAL_1MINUTE, "1 day ago UTC"
# ):
#     print(kline)
#     # do something with the kline


# # Get account info
# info = client.get_account()
# print(info)

# # Get asset balance
# balance = client.get_asset_balance(asset="USDT")
# print(balance)

# # Get account status
# status = client.get_account_status()
# print(status)

# # Get trades
# trades = client.get_my_trades(symbol="BTCUSDT")
# print(trades)

# Get trade fees

# # get fees for all symbols
# fees = client.get_trade_fee()

# # get fee for one symbol
# fees = client.get_trade_fee(symbol="BTCUSDT")
# print(fees)

# # Get asset details
# details = client.get_asset_details()
# print(details)

# # Get dust log
# log = client.get_dust_log()
# print(log)

# Transfer dust
# transfer = client.transfer_dust(asset='BNZ')

# Get Asset Dividend History

# history = client.get_asset_dividend_history()


# # Get Kline/Candlesticks
# candles = client.get_klines(symbol="BNBBTC", interval=Client.KLINE_INTERVAL_30MINUTE)
# print(candles)

# # Get 2 candlesticks- the running and the last closed candlestick
# candles = client.get_klines(
#     symbol="BTCUSDT", interval=Client.KLINE_INTERVAL_1MINUTE, limit=2
# )
# print(candles)


# # Binance servertime (for connection purposes)
# time_res = client.get_server_time()
# print(time_res)
