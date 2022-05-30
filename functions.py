##!/usr/bin/env python3
# This file contains all functions.
from datetime import datetime
import os.path
import sqlite3
from binance.client import Client
import config
import secrets

client = Client(secrets.API_KEY, secrets.API_SECRET)

# ============= Database related functions =============

def check_table(symbol, time_frame):
    """Function that checks if the table for the given coin and timeframe exists in the database."""
    conn = sqlite3.connect(config.data_location+ symbol + ".db")
    c = conn.cursor()
    db_time_frame = "_" + time_frame
    # Count if there are tables
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
    # Create the database if not existing yet
    conn = sqlite3.connect(config.data_location+ symbol + ".db")
    print(f"Database {symbol} created")
    # Call function to create a table after creation of a database
    create_table(symbol, time_frame)
    conn.commit()
    conn.close()

def check_db(symbol, time_frame):
    """Function that checks if symbol database exists."""
    if os.path.exists(config.data_location+ symbol + ".db"):
        check_table(symbol, time_frame)
    else:
        # Database does not exist, call db create function.
        create_db(symbol, time_frame)

def create_table(symbol, time_frame):
    """Function that creates the missing timeframe table."""
    # Connect to the database
    conn = sqlite3.connect(config.data_location+ symbol + ".db")
    c = conn.cursor()
    # Create the database, based on the timeframe
    db_time_frame = "_" + time_frame
    c.execute(
        # Create the table in the database in the format of the Binance exchange
        "CREATE TABLE "
        + db_time_frame
        + " (openTime integer PRIMARY KEY,open integer,high real,low real,close real,volume integer,closeTime integer,quoteAssetVolume integer,numberOfTrades integer,takerBuyBaseAssetVolume text,takerBuyQuoteAssetVolume text,ignore text, dow text)"
    )
    print(f"Table {symbol} {time_frame} created.")
    conn.commit()
    conn.close()

# ============= Data related functions =============

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
    Arguments below come from the fetch_data function.

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
    conn = sqlite3.connect(config.data_location+ symbol + ".db")
    db_time_frame = "_" + time_frame
    c = conn.cursor()
    # Try to insert the data into the database
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
        # But if data already exists (tablekey = OpenTime)
        # then then show an error and leave the data as it is.
        print(f"{symbol}- {time_frame} record {openTime} already exists.")
    conn.commit()
    conn.close()

def fetch_base_data(symbol, time_frame):
    """This function fetches a base of klines from exchange and prepares it for importing in
    the database with the add_record function."""
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

    # Get the recent X candles from the binance API
    recent_candles = client.get_klines(symbol=symbol, interval=interval, limit=500)
    # Assign candle values to variables
    for recent_candle in recent_candles:
        # print(recent_candle)
        # Take each position in the candle output 
        # and add it to a variable to prepare it for entering
        # in a database with the add_record function.
        #
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
        # using the function and the variables below.
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

def get_needle(symbol, time_frame):
    """This function connects to the database and fetches the most current database entry.

    Args:
        symbol (string): Symbol of the cryptocurrency

    Returns:
        integer: Location of the last database candle in the API output
    """
    conn = sqlite3.connect(config.data_location+ symbol + ".db")
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