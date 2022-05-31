##!/usr/bin/env python3
# This file contains all candle data related functions.

# Import modules
import os
import sqlite3
from config import *
from database import add_record


def download_candle_history():
    pass
    # Download candle data history amount set in config file


def check_candle_data(symbol, time_frame):
    """
    This function connects to the database and fetches the most current database entry.
    
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
        print("Last entry is: " + str(last_entry) + "\nFetching last full candle(s).")
        return last_entry
    except:
        # No data in database. Make placeholder label. Then fetch all missing data from the exchange.
        last_entry = 0
        print("Last entry is: " + str(last_entry) + "\nFetching historical data.")
    conn.commit()
    conn.close()


def download_last_candle():
    pass
    # Download the last full candle from the exchange
