##!/usr/bin/env python3
# This file contains all functions.
from datetime import datetime
import os.path
import sqlite3
from binance.client import Client
import config

client = Client(config.API_KEY, config.API_SECRET)

# ============= Database related functions =============
data_location = "./data/"


def check_db(symbol, time_frame):
    """Function that checks if symbol database exists."""
    if os.path.exists(data_location + symbol + ".db"):
        check_table(symbol, time_frame)
    else:
        # Database does not exist, call db create function.
        create_db(symbol, time_frame)


def check_table(symbol, time_frame):
    """Function that checks if the table for the given timeframe exists in the database."""
    conn = sqlite3.connect(data_location + symbol + ".db")
    c = conn.cursor()
    db_time_frame = "_" + time_frame
    c.execute(
        "SELECT count(name) FROM sqlite_master WHERE type='table' AND name=(?)",
        (db_time_frame,),
    )
    # get the count of tables with the name db_time_frame
    # if the count is 1, then table exists, if 0 then make it.
    if c.fetchone()[0] == 1:
        pass
    else:
        # Table does not exist, call table create function.
        create_table(symbol, time_frame)


def create_db(symbol, time_frame):
    """Function that creates the missing symbol database."""
    conn = sqlite3.connect(data_location + symbol + ".db")
    print(f"Database {symbol} created")
    create_table(symbol, time_frame)
    conn.commit()
    conn.close()


def create_table(symbol, time_frame):
    """Function that creates the missing timeframe table."""
    conn = sqlite3.connect(data_location + symbol + ".db")
    c = conn.cursor()
    db_time_frame = "_" + time_frame
    c.execute(
        "CREATE TABLE "
        + db_time_frame
        + " (openTime integer PRIMARY KEY,open text,high text,low text,close text,volume text,closeTime integer,quoteAssetVolume text,numberOfTrades integer,takerBuyBaseAssetVolume text,takerBuyQuoteAssetVolume text,ignore text, dow text)"
    )
    print(f"Table {symbol} {time_frame} created.")
    conn.commit()
    conn.close()


def add_record(
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
):
    """This function is used to add a new record to the symbols database.

    Args:
        symbol (string): Symbol of the crypto currency
        openTime (int): Datetime open in unix format (note: Binance uses milliseconds)
        open (string): Candle open price
        high (string): Candle highest price
        low (string): Candle lowest price
        close (string): Candle close price
        volume (string): Volume
        closeTime (integer): Datetime close in unix format (note: Binance uses milliseconds)
        quoteAssetVolume (string):
        numberOfTrades (string):
        takerBuyBaseAssetVolume (string):
        takerBuyQuoteAssetVolume (string):
        ignore (string):
    """
    conn = sqlite3.connect(data_location + symbol + ".db")
    db_time_frame = "_" + time_frame
    c = conn.cursor()
    # print(
    #     symbol,
    #     time_frame,
    #     openTime,
    #     open,
    #     high,
    #     low,
    #     close,
    #     volume,
    #     closeTime,
    #     quoteAssetVolume,
    #     numberOfTrades,
    #     takerBuyBaseAssetVolume,
    #     takerBuyQuoteAssetVolume,
    #     ignore,
    # )
    try:
        c.execute(
            "INSERT INTO " + db_time_frame + " VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",
            (
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
            ),
        )
    except sqlite3.IntegrityError:
        # If data already exists (tablekey = OpenTime)
        print(f"{symbol}- {time_frame} record {openTime} already exists.")
    conn.commit()
    conn.close()


# ============= ... functions =============


def fetch_data(symbol, time_frame):
    """This function fetches recent klines from exchange and enters the data in the database."""
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

    recent_candles = client.get_klines(symbol=symbol, interval=interval, limit=500)
    # Assign candle values to variables
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
        dow = datetime.fromtimestamp(openTime / 1000).strftime("%A")
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
        )
