# This file  will contain all dataframe functions
import sqlite3
import pandas as pd
from config import candle_history, data_location


def create_dataframe(symbol, time_frame):
    """
    This function connects to the database of the given pair and then creates a dataframe
    for further strategy analysis and signalling.
    """
    
    # Connect to the database of the given symbol and then create a dataframe of the given time_frame
#    conn = sqlite3.connect("file:./data/" + symbol + ".db?mode=ro", uri=True)
    conn = sqlite3.connect("file:" + data_location + symbol + ".db?mode=ro", uri=True)
    df = pd.read_sql_query("SELECT * FROM (SELECT openTime,open,high,low,close,volume,dow,color,humandate FROM _" + time_frame +" ORDER BY openTime DESC LIMIT " + str(candle_history) + ") sub ORDER BY openTime ASC", conn)
    conn.close()
    
    # Change Unix time to human readable time
    df["openTime"] = pd.to_datetime(df["openTime"], unit="s")

    # print(symbol, time_frame)
    # print(df)

    return df


# def heiken_ashi(df):
#     """_summary_
#     Function that creates an Heiken Ashi candlestick dataframe.
#     Has to be developed further.

#     Args:
#         df (_type_): _description_

#     Returns:
#         _type_: _description_
#     """
#     df_ha = df.copy()
    
#     for i in range(df_ha.shape[0]):
#         if i > 0:
#             df_ha.loc[df_ha.index[i],'open'] = (df['open'][i-1] + df['close'][i-1])/2
            
#             df_ha.loc[df_ha.index[i],'close'] = (df['open'][i] + df['close'][i] + df['low'][i] +  df['high'][i])/4
            
#             df_ha = df_ha.iloc[1:,:]

#     print(df_ha)

#     return df_ha
