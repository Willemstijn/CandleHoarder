##!/usr/bin/env python3
# This file contains all configurations for the hoarder.

from binance.client import Client
import secrets

# Enter the location where the databases should exist / be created.
data_location = "./data/"

# Enter all the crypto pairs you want to watch in this array.
# symbols = ["BTCUSDT", "ETHUSDT", "ADAUSDT", "XRPUSDT"]
# symbols = ["BTCUSDT"]
symbols = ["BTCUSDT",
        "ETHUSDT",
        "BNBUSDT",
        "SOLUSDT",
        "ADAUSDT",
        "XRPUSDT",
        "LUNAUSDT",
        "DOTUSDT",
        "AVAXUSDT",
        "DOGEUSDT",
        "SHIBUSDT",
        "MATICUSDT",
        "ALGOUSDT",
        "LTCUSDT",
        "LINKUSDT",
        "DAIUSDT",
        "NEARUSDT",
        "BCHUSDT",
        "ATOMUSDT",
        "TRXUSDT",
        "XLMUSDT",
        "FTMUSDT",
        "MANAUSDT",
        "AXSUSDT",
        "HBARUSDT",
        "VETUSDT",
        "FTTUSDT",
        "SANDUSDT",
        "ICPUSDT",
        "FILUSDT",
        "THETAUSDT",
        "EGLDUSDT",
        "ETCUSDT",
        "HNTUSDT",
        "XMRUSDT",
        "XTZUSDT",
        "AAVEUSDT",
        "KLAYUSDT",
        "ONEUSDT",
        "GRTUSDT",
        "GALAUSDT",
        "EOSUSDT",
        "CAKEUSDT",
        "STXUSDT",
        "FLOWUSDT",
        "BTTUSDT",
        "LRCUSDT",
        "CRVUSDT",
        "KSMUSDT",
        "MKRUSDT",
        "ENJUSDT",
        "QNTUSDT",
        "XECUSDT",
        "AMPUSDT",
        "ZECUSDT",
]

# Select a timeframe to watch on.
# Available timeframes are: 1m, 3m, 5m, 15m, 30m, 1h, 2h, 4h, 6h, 8h, 12h, 1d, 3d, 1w, 1M.
time_frames = ["1d"]

# Enter amount of historical data to fetch for initial candle data download
candle_history = 10

# Client key & secret for downloading data through the API exchange
client = Client(secrets.BINANCE_API_KEY, secrets.BINANCE_API_SECRET)