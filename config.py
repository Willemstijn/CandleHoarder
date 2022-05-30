#!/usr/bin/env python3
# This is the config file for the Opportunity knocks warning bot.

import secrets

# Enter location of databases to place
data_location = "./data/"

# Enter all the crypto pairs you want to watch in this array.
symbols = ["BTCUSDT", "ETHUSDT", "ADAUSDT", "XRPUSDT"]

# Select a timeframe to watch on.
# Available timeframes are: 1m, 3m, 5m, 15m, 30m, 1h, 2h, 4h, 6h, 8h, 12h, 1d, 3d, 1w, 1M.
time_frames = [
    "1h",
    "4h",
    "1d",
    "3d",
    "1w",
]

# Binance keys - KEEP THIS SECRET!! -
API_KEY = secrets.api_key
API_SECRET = secrets.api_secret
