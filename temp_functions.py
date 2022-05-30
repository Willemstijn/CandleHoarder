# These functions come from the CryptoMaven program

##!/usr/bin/env python3
# this file contains all classes and functions related to candle data
# extracted from the Binance exchange
import json
from datetime import datetime

import requests

import config
import database


class candle:
    """The candle class is used to get Binance symbol data in a standarized way.
    Please refer to the official Binance API docs for more information on the Kline/Candlestick data on:
    https://github.com/binance-exchange/binance-official-api-docs/blob/master/rest-api.md#enum-definitions
    """

    def __init__(self, symbol, time_frame):
        self.symbol = symbol
        self.timeframe = time_frame

    def printCandle(self, when):
        """This function prints the current or last candle data of the symbol to the screen."""
        if when == "current":
            listPosition = -1
        elif when == "last":
            listPosition = -2
        # This section has to be copied into each function
        url = f"https://api.binance.com/api/v3/klines?symbol={self.symbol}&interval={self.timeframe}"
        r = requests.get(url)
        symbol_json = r.json()
        symbol = symbol_json[listPosition]
        # ===
        self.openTime = symbol[0]
        self.open = symbol[1]
        self.high = symbol[2]
        self.low = symbol[3]
        self.close = symbol[4]
        self.volume = symbol[5]
        self.closeTime = symbol[6]
        self.quoteAssetVolume = symbol[7]
        self.numberOfTrades = symbol[8]
        self.takerBuyBaseAssetVolume = symbol[9]
        self.takerBuyQuoteAssetVolume = symbol[10]
        self.ignore = symbol[11]
        openTime_hr = datetime.fromtimestamp(self.openTime // 1000)
        closeTime_hr = datetime.fromtimestamp(self.closeTime // 1000)
        print(
            f"Symbol: {self.symbol}, Open time: {openTime_hr}, Open: {self.open}, High: {self.high}, Low: {self.low}, Close: {self.close}, Volume: {self.volume}, Close time: {closeTime_hr}"
        )

    def checkHistory(self):
        """This function checks if there is a difference between the last database entry and the 2nd last candle from the API (500-2).
        If there is a difference, it tries to find out the dataset that is missing and will download this so that there will be
        no missing candles between last candle and API output. If there is no candle data found in the database, it assumes there is
        no candle history and it will download all API data up untill the last candle."""
        # Datapoints of the klines endpoint:
        # 1m has 0-499, 5m has 0-499, 1h has 0-499, 4h has 0-499, 1d has 0-499,
        # 1w has 0-162 (and growing?), 1M has 0-37 (and growing?)

        url = f"https://api.binance.com/api/v3/klines?symbol={self.symbol}&interval={self.timeframe}"
        r = requests.get(url)
        symbol_json = r.json()  # grab complete history of coin
        needle = database.get_needle(self.symbol)
        # Get datetime field from all candles in history and put in list.
        symbol_dates = []

        for symbols in symbol_json:
            timestamp = symbols[0]
            symbol_dates.append(timestamp)

        # search list for last database entry. When there, check for location and download missing data.
        # When not in list, download complete list to database.
        # if symbol_dates.index(needle):
        try:
            if symbol_dates.index(needle):
                needle_pos = symbol_dates.index(needle)
                # Pos 498 is the most recent closed (!) candle. Pos 499 candle is current candle.
                if needle_pos == 497:
                    print(
                        f"Checking timestamp {needle} @ pos. {needle_pos} for {self.symbol}."
                    )
                else:
                    print(
                        f"Checking timestamp {needle} @ pos. {needle_pos} for {self.symbol}."
                    )
                    self.get_history(needle_pos)
        # except Exception as e:
        except:
            # Needle has not been detected in database
            print(f"Empty database or more than 500 missing candles for {self.symbol}.")
            needle = 0
            needle_pos = needle
            self.get_history(needle_pos)

    def update(self):
        """This function will be used to update the symbol database with data of
        the last closed candle on the chosen timeframe"""
        # This section has to be copied into each function
        url = f"https://api.binance.com/api/v3/klines?symbol={self.symbol}&interval={self.timeframe}"
        r = requests.get(url)
        symbol_json = r.json()
        symbol = symbol_json[-2]
        # ===
        self.openTime = symbol[0]
        self.open = symbol[1]
        self.high = symbol[2]
        self.low = symbol[3]
        self.close = symbol[4]
        self.volume = symbol[5]
        self.closeTime = symbol[6]
        self.quoteAssetVolume = symbol[7]
        self.numberOfTrades = symbol[8]
        self.takerBuyBaseAssetVolume = symbol[9]
        self.takerBuyQuoteAssetVolume = symbol[10]
        self.ignore = symbol[11]

        # candle information above will be inserted in database add record function
        database.add_record(
            self.symbol,
            self.openTime,
            self.open,
            self.high,
            self.low,
            self.close,
            self.volume,
            self.closeTime,
            self.quoteAssetVolume,
            self.numberOfTrades,
            self.takerBuyBaseAssetVolume,
            self.takerBuyQuoteAssetVolume,
            self.ignore,
        )
        openTime_hr = datetime.fromtimestamp(self.openTime // 1000)
        closeTime_hr = datetime.fromtimestamp(self.closeTime // 1000)
        print(
            f"Getting candle {self.symbol}, time: {openTime_hr}: OHLCV: {self.open}-{self.high}-{self.low}-{self.close}-{self.volume}"
        )

    def get_history(self, needle_pos):
        """This function downloads all the data between the given needle position and the most current closed candle.
        Function will be activated if the candle.checkHistory detects an anomaly between the most
        current db entry and Binance kline data."""
        url = f"https://api.binance.com/api/v3/klines?symbol={self.symbol}&interval={self.timeframe}"
        r = requests.get(url)
        symbol_json = r.json()
        starting_point = needle_pos + 1
        ending_point = len(symbol_json) - 3
        history_range = list(range(starting_point, ending_point, 1))

        for history_item in history_range:
            symbol = symbol_json[history_item]
            self.openTime = symbol[0]
            self.open = symbol[1]
            self.high = symbol[2]
            self.low = symbol[3]
            self.close = symbol[4]
            self.volume = symbol[5]
            self.closeTime = symbol[6]
            self.quoteAssetVolume = symbol[7]
            self.numberOfTrades = symbol[8]
            self.takerBuyBaseAssetVolume = symbol[9]
            self.takerBuyQuoteAssetVolume = symbol[10]
            self.ignore = symbol[11]

            # candle information above will be inserted in database add record function
            database.add_record(
                self.symbol,
                self.openTime,
                self.open,
                self.high,
                self.low,
                self.close,
                self.volume,
                self.closeTime,
                self.quoteAssetVolume,
                self.numberOfTrades,
                self.takerBuyBaseAssetVolume,
                self.takerBuyQuoteAssetVolume,
                self.ignore,
            )
        print(f"Importing missing history range {history_range} for {self.symbol}.")


##!/usr/bin/env python3
# This file contains all classes and functions related to database related work.
import os.path
import sqlite3

import config as cfg

data_location = "./data/"
config_symbols = cfg.symbols
time_frame = cfg.time_frame


def create_db():
    """This function checks if the database for the current coin exists. It will create the database if it does not.
    Next there will be a check if the table of the chosen time frame exists. It will create the table if it does not.
    """
    for symbol in config_symbols:
        # check if database exists
        if os.path.exists(data_location + symbol + ".db"):
            # print(f"Database {symbol} already exists")
            # check if table exists
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
                c.execute(
                    "CREATE TABLE "
                    + db_time_frame
                    + " (openTime integer PRIMARY KEY,open text,high text,low text,close text,volume text,closeTime integer,quoteAssetVolume text,numberOfTrades integer,takerBuyBaseAssetVolume text,takerBuyQuoteAssetVolume text,ignore text)"
                )
                print(f"Table {time_frame} created.")
            conn.commit()
            conn.close()
        else:
            # create symbol database
            conn = sqlite3.connect(data_location + symbol + ".db")
            print(f"Database {symbol} created")
            db_time_frame = "_" + time_frame
            c = conn.cursor()
            c.execute(
                "CREATE TABLE "
                + db_time_frame
                + " (openTime integer PRIMARY KEY,open text,high text,low text,close text,volume text,closeTime integer,quoteAssetVolume text,numberOfTrades integer,takerBuyBaseAssetVolume text,takerBuyQuoteAssetVolume text,ignore text)"
            )
            conn.commit()
            conn.close()


def add_record(
    symbol,
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
            "INSERT INTO " + db_time_frame + " VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",
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
            ),
        )
    except sqlite3.IntegrityError:
        # If data already exists (tablekey = OpenTime)
        print("record already exists")
    conn.commit()
    conn.close()


def get_needle(symbol):
    """This function connects to the database and fetches the most current database entry.

    Args:
        symbol (string): Symbol of the cryptocurrency

    Returns:
        integer: Location of the last database candle in the API output
    """
    conn = sqlite3.connect(data_location + symbol + ".db")
    c = conn.cursor()
    db_time_frame = "_" + time_frame
    last_db_entry = c.execute(
        f"SELECT openTime FROM {db_time_frame} ORDER BY openTime DESC LIMIT 1;"
    )
    # Change the <sqlite3.Cursor object at XXXX> an actual readable needle variable
    try:
        needle = c.fetchall()[0][0]
        return needle
    except:
        # No data in database. Make placeholder label.
        needle = 0
    conn.commit()
    conn.close()


# test if last database entry will be looked up correctly
# print(get_last_db_entry("ADAUSDT"))