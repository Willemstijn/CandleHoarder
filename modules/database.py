##!/usr/bin/env python3
# This file contains all database related functions.

# Import modules
import sys
import os
import sqlite3
from config import *

# Path to modules
sys.path.insert(1, "./modules/")


def create_table(symbol, time_frame):
    """Function that creates the missing timeframe table."""
    # Create a connector and cursor for the sqlite database.
    conn = sqlite3.connect(data_location + symbol + ".db")
    c = conn.cursor()
    db_time_frame = "_" + time_frame
    # Create the table for receiving candle data.
    c.execute(
        "CREATE TABLE "
        + db_time_frame
        + "(openTime integer PRIMARY KEY,open integer,high real,low real,close real,volume integer,closeTime integer,quoteAssetVolume integer,numberOfTrades integer,takerBuyBaseAssetVolume integer,takerBuyQuoteAssetVolume integer,ignore text, dow text, color text, humandate integer)"
    )
    # Confirmation to screen.
    print(f"Table {symbol} {time_frame} created.")
    # Commit changes and close connection to the database
    conn.commit()
    conn.close()


def check_table(symbol, time_frame):
    """Function that checks if the table for the given timeframe exists in the database.
    If it does not exist, then it creates the table for the given pair and timeframe."""
    conn = sqlite3.connect(data_location + symbol + ".db")
    c = conn.cursor()
    db_time_frame = "_" + time_frame
    # After connection to the database, check if tables exist. 
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
    # Connection to a non existing database actually creates it.
    conn = sqlite3.connect(data_location + symbol + ".db")
    print(f"Database {symbol} created")
    # After the database is created, check if there is a table for receiving candle data.
    check_table(symbol, time_frame)
    conn.commit()
    conn.close()


def check_db(symbol, time_frame):
    """
    Function that checks if symbol database exists.
    If not, then it creates the database.
    """
    # Check if a database exists.
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
    humandate
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
    # Connect to the database.
    conn = sqlite3.connect(data_location + symbol + ".db")
    db_time_frame = "_" + time_frame
    c = conn.cursor()
    # Receive the candle data and insert it into the database.
    try:
        c.execute(
            "INSERT INTO " + db_time_frame + " VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
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
                humandate
            ),
        )
    except sqlite3.IntegrityError:
        # If data already exists (tablekey = OpenTime)
        print(f"{symbol}- {time_frame} record {openTime} already exists.")
    conn.commit()
    conn.close()