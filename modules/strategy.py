# This file contains all the strategies that will be calculated and plotted
import pandas as pd
import pandas_ta as pta
import ta as ta
import numpy as np

def test(symbol, time_frame, df):
    print(symbol, time_frame)
    print(df)

def superhilo(df):
    # macd
    fast = 12
    slow = 26
    smooth = 9
    df["macd"] = pta.macd(close=df["close"], fast=fast, slow=slow, signal=smooth, offset=None)[f"MACD_{fast}_{slow}_{smooth}"]
    df["macds"] = pta.macd(close=df["close"], fast=fast, slow=slow, signal=smooth, offset=None)[f"MACDs_{fast}_{slow}_{smooth}"]
    df["macdh"] = pta.macd(close=df["close"], fast=fast, slow=slow, signal=smooth, offset=None)[f"MACDh_{fast}_{slow}_{smooth}"]

    # supertrend
    length = 10
    multiplier = 4.5
    df["supertrend_buy"] = pta.supertrend(high=df["high"],low=df["low"],close=df["close"],length=length,multiplier=multiplier,)[f"SUPERTd_{length}_{multiplier}"]
    df["supertrend"] = pta.supertrend(high=df["high"],low=df["low"],close=df["close"],length=length,multiplier=multiplier,)[f"SUPERT_{length}_{multiplier}"]

    # hilo
    highl = 13
    lowl = 21
    df["hilo"] = pta.hilo(high=df["high"],low=df["low"],close=df["close"],high_length=highl,low_length=lowl,mamode=None,offset=None,)[f"HILO_{highl}_{lowl}"]

    print(df)














# def check_swing_strategy(symbol, timeframe, df):
#     """Function that checks the last candle close and returns signals when a
#     change in advice is detected."""

#     # Get the second to last entry in the dataframe column with advice
#     # This is the last full closing day.
#     change = df.iloc[-2]["POS_adv_changed"]
#     advice = df.iloc[-2]["POS_adv"]
#     close = df.iloc[-2]["close"].round(2)

#     # If change field is false (not the same as the previous advice),
#     # then the advice has been changed and a warning should be created.
#     if change == False:
#         # return swing strategy advice
#         signal_field = "{} signal {} ({}).\nClose: {},\n\n".format(
#             advice, symbol, timeframe, close
#         )
#         return signal_field