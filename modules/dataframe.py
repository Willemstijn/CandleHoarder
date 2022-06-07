# This file  will contain all dataframe functions
import sqlite3
import pandas as pd

def create_dataframe(symbol, time_frame):
    """
    This function connects to the database of the given pair and then creates a dataframe
    for further strategy analysis and signalling.
    """
    
    # Connect to the database of the given symbol and then create a dataframe of the given time_frame
    conn = sqlite3.connect("file:./data/" + symbol + ".db?mode=ro", uri=True)
    df = pd.read_sql_query("SELECT * FROM (SELECT openTime,open,high,low,close,volume,dow,color,humandate FROM _" + time_frame +" ORDER BY openTime DESC LIMIT 10) sub ORDER BY openTime ASC", conn)
    conn.close()
    
    # Do some modifications to the dataframe so that it is ready for further analysis

    # Change Unix time to human readable time
    df["openTime"] = pd.to_datetime(df["openTime"], unit="s")

    # print(symbol, time_frame)
    # print(df)

    return df