##!/usr/bin/env python3
# This file contains all candle data related functions.

# Import modules
import sys
import sqlite3
from calendar import day_abbr, month
from time import time
from turtle import onclick
from config import *
from modules.database import add_record
from datetime import datetime

# Path to modules
sys.path.insert(1, "./modules/")


def download_candle_history(symbol, time_frame):
    """
    This function fetches historical klines from exchange and enters the data in the database.
    """
    print("No data found! Downloading history for " + symbol + " on " + time_frame)
    if time_frame == "1m":
        interval = Client.KLINE_INTERVAL_1MINUTE
    elif time_frame == "3m":
        interval = Client.KLINE_INTERVAL_3MINUTE
    elif time_frame == "5m":
        interval = Client.KLINE_INTERVAL_5MINUTE
    elif time_frame == "15m":
        interval = Client.KLINE_INTERVAL_15MINUTE
    elif time_frame == "30m":
        interval = Client.KLINE_INTERVAL_30MINUTE
    elif time_frame == "1h":
        interval = Client.KLINE_INTERVAL_1HOUR
    elif time_frame == "4h":
        interval = Client.KLINE_INTERVAL_4HOUR
    elif time_frame == "6h":
        interval = Client.KLINE_INTERVAL_6HOUR
    elif time_frame == "8h":
        interval = Client.KLINE_INTERVAL_8HOUR
    elif time_frame == "12h":
        interval = Client.KLINE_INTERVAL_12HOUR
    elif time_frame == "1d":
        interval = Client.KLINE_INTERVAL_1DAY
    elif time_frame == "3d":
        interval = Client.KLINE_INTERVAL_3DAY
    elif time_frame == "1w":
        interval = Client.KLINE_INTERVAL_1WEEK
    elif time_frame == "1M":
        interval = Client.KLINE_INTERVAL_1MONTH

    # After determining the timeframe get candle data (klines) with help of the binance Python module.
    recent_candles = client.get_klines(symbol=symbol, interval=interval, limit=candle_history)
    # Pop last entry from list. This candle is not closed but active.
    recent_candles.pop(-1)
    # Assign candle values to variables for inserting into the database.
    for recent_candle in recent_candles:
        openTime = recent_candle[0] // 1000
        open = recent_candle[1]
        high = recent_candle[2]
        low = recent_candle[3]
        close = recent_candle[4]
        volume = recent_candle[5]
        closeTime = recent_candle[6] // 1000
        quoteAssetVolume = recent_candle[7]
        numberOfTrades = recent_candle[8]
        takerBuyBaseAssetVolume = recent_candle[9]
        takerBuyQuoteAssetVolume = recent_candle[10]
        ignore = recent_candle[11]
        dow = datetime.fromtimestamp(openTime).strftime("%A")
        humandate = datetime.fromtimestamp(openTime).strftime("%Y%m%d")
        if open > close:
            color = "Red"
        else:
            color = "Green"
        # Create an entry in the specific database table with the variables above.
        add_record(
            symbol,
            time_frame,
            openTime,
            open,
            high,
            low,
            close,
            volume,
            closeTime,
            quoteAssetVolume,
            numberOfTrades,
            takerBuyBaseAssetVolume,
            takerBuyQuoteAssetVolume,
            ignore,
            dow,
            color,
            humandate
        )


def download_last_candle(symbol, time_frame, is_entry):
    """
    This function checks for the last database entry and then downloads the candles from that entry on.
    If the last entry does not exist within the last 100 (maximum) candles, then assume something went wrong 
    and recreate the complete database from scratch.
    """
    print("History found! Download latest entries for " + symbol + " on " + time_frame)
    # Determine the timeframe
    if time_frame == "1m":
        interval = Client.KLINE_INTERVAL_1MINUTE
    elif time_frame == "3m":
        interval = Client.KLINE_INTERVAL_3MINUTE
    elif time_frame == "5m":
        interval = Client.KLINE_INTERVAL_5MINUTE
    elif time_frame == "15m":
        interval = Client.KLINE_INTERVAL_15MINUTE
    elif time_frame == "30m":
        interval = Client.KLINE_INTERVAL_30MINUTE
    elif time_frame == "1h":
        interval = Client.KLINE_INTERVAL_1HOUR
    elif time_frame == "4h":
        interval = Client.KLINE_INTERVAL_4HOUR
    elif time_frame == "6h":
        interval = Client.KLINE_INTERVAL_6HOUR
    elif time_frame == "8h":
        interval = Client.KLINE_INTERVAL_8HOUR
    elif time_frame == "12h":
        interval = Client.KLINE_INTERVAL_12HOUR
    elif time_frame == "1d":
        interval = Client.KLINE_INTERVAL_1DAY
    elif time_frame == "3d":
        interval = Client.KLINE_INTERVAL_3DAY
    elif time_frame == "1w":
        interval = Client.KLINE_INTERVAL_1WEEK
    elif time_frame == "1M":
        interval = Client.KLINE_INTERVAL_1MONTH

    # After determining the timeframe get candle data (klines) with help of the binance Python module.
    last_candles = client.get_klines(symbol=symbol, interval=interval, limit=10)
    # Pop last entry from list. This candle is not closed but active.
    last_candles.pop(-1)
    # check if the last candle in the database is in the just downloaded last candles list
    # and determine the position of the newest candle(s)
    temp = []
    for last_candle in last_candles:
        temp.append(last_candle[0]/1000)
    # get the exact position of the NEW candle in this downloaded list
    position = temp.index(is_entry) + 1
    # Now add all the entries from the original last_candles list to the database
    # from the newest position, therefore also adding possible missing candles.
    # First create a sublist of the original downloaded list containing only the candles to import.
    import_candles = last_candles[position:]
    # Then walk over the sublist and import every candle into the database.
    for import_candle in import_candles:
        openTime = import_candle[0] // 1000
        open = import_candle[1]
        high = import_candle[2]
        low = import_candle[3]
        close = import_candle[4]
        volume = import_candle[5]
        closeTime = import_candle[6] // 1000
        quoteAssetVolume = import_candle[7]
        numberOfTrades = import_candle[8]
        takerBuyBaseAssetVolume = import_candle[9]
        takerBuyQuoteAssetVolume = import_candle[10]
        ignore = import_candle[11]
        dow = datetime.fromtimestamp(openTime).strftime("%A")
        humandate = datetime.fromtimestamp(openTime).strftime("%Y%m%d")
        if open > close:
            color = "Red"
        else:
            color = "Green"
        # Create an entry in the specific database table
        add_record(
            symbol,
            time_frame,
            openTime,
            open,
            high,
            low,
            close,
            volume,
            closeTime,
            quoteAssetVolume,
            numberOfTrades,
            takerBuyBaseAssetVolume,
            takerBuyQuoteAssetVolume,
            ignore,
            dow,
            color,
            humandate
        )


def check_candle_data(symbol, time_frame):
    """
    This function connects to the database and checks if there is candle data present.
    If not, then it calls the candle_download_history function.
    
    Args:
        symbol (string): Symbol of the pair
        time_frame (string): Time frame of the pair
    Returns:
        integer: Location of the last database candle in the API output
    """
    pass
    conn = sqlite3.connect(data_location + symbol + ".db")
    c = conn.cursor()
    db_time_frame = "_" + time_frame
    # After connection to database, sort the database on openTime (descending) and
    # fetch the first entry.
    last_db_entry = c.execute(
        f"SELECT openTime FROM {db_time_frame} ORDER BY openTime DESC LIMIT 1;"
    )
    # print(last_db_entry) # returns an object instead of a value
    # Change the <sqlite3.Cursor object at XXXX> an actual readable last_entry variable
    try:
        last_entry = c.fetchall()[0][0]
        # print("Last entry is: " + str(last_entry))
        return last_entry
    except:
        # No data in database. Make placeholder label. Then fetch all missing data from the exchange.
        last_entry = 0
        # print("Last entry is: " + str(last_entry))
        download_candle_history(symbol, time_frame)
        return last_entry   
    conn.commit()
    conn.close()

