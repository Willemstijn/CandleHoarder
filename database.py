##!/usr/bin/env python3
# This file contains all database related functions.

# Import modules
import os
import sqlite3
from config import *


def create_table(symbol, time_frame):
    """Function that creates the missing timeframe table."""
    conn = sqlite3.connect(data_location + symbol + ".db")
    c = conn.cursor()
    db_time_frame = "_" + time_frame
    c.execute(
        "CREATE TABLE "
        + db_time_frame
        + "(openTime integer PRIMARY KEY,open integer,high real,low real,close real,volume integer,closeTime integer,quoteAssetVolume integer,numberOfTrades integer,takerBuyBaseAssetVolume integer,takerBuyQuoteAssetVolume integer,ignore text, dow text, color text)"
    )
    print(f"Table {symbol} {time_frame} created.")
    conn.commit()
    conn.close()


def check_table(symbol, time_frame):
    """Function that checks if the table for the given timeframe exists in the database.
    If it does not exist, then it creates the table for the given pair and timeframe."""
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
        # Table does not exist for the given timeframe, call table create function.
        create_table(symbol, time_frame)


def create_db(symbol, time_frame):
    """Function that creates the missing symbol database."""
    conn = sqlite3.connect(data_location + symbol + ".db")
    print(f"Database {symbol} created")
    # After the database is created, check if the table is there
    check_table(symbol, time_frame)
    conn.commit()
    conn.close()


def check_db(symbol, time_frame):
    """Function that checks if symbol database exists.
    If not, then it creates the database. """
    # print(data_location)
    if os.path.exists(data_location + symbol + ".db"):
        # If database exists, check if the table for the given timeframe exists
        check_table(symbol, time_frame)
    else:
        # Database does not exist, call db create function above.
        create_db(symbol, time_frame)

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
    color,
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
    try:
        c.execute(
            "INSERT INTO " + db_time_frame + " VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
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
                color,
            ),
        )
    except sqlite3.IntegrityError:
        # If data already exists (tablekey = OpenTime)
        print(f"{symbol}- {time_frame} record {openTime} already exists.")
    conn.commit()
    conn.close()