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

    # Determine conditions that create signals
    # ========================================
    # hilo
    df["hilo_buy"] = df["close"] > df["hilo"]
    # macd
    df["macd_buy"] = df["macd"] > df["macds"]
    # supertrend
    df["supertrend_buy"] = df["close"] > df["supertrend"]
    # supertrend_buy already has 1 for true (buy) signal
    
    print(df[["openTime","open","high","low","close","volume","supertrend_buy","macd_buy","hilo_buy",]].tail(10))



    # # Function below actually creates the columns with buy/sell signals and corresponding prices
    # # ==========================================================================================
    # def buy_sell(df):
    #     """Function that determines the buy / sell signals based on the indicators."""
    #     sigPriceBuy = []
    #     sigPriceSell = []
    #     signal = []
    #     flag = -1

    #     for i in range(len(df)):
    #         # Buy Signal if MACD, supertrend_buy and hilo are true
    #         if (
    #             (df["hilo_buy"][i] == True)
    #             & (df["macd_buy"][i] == True)
    #             & (df["supertrend_buy"][i] == 1)
    #         ):
    #             if flag != 1:
    #                 sigPriceBuy.append(df["close"][i])
    #                 sigPriceSell.append(np.NaN)
    #                 signal.append("buy")
    #                 flag = 1
    #             else:
    #                 sigPriceBuy.append(np.NaN)
    #                 sigPriceSell.append(np.NaN)
    #                 signal.append("neutral")
    #         # Sell if MACD has bearish crossover
    #         elif ((df["hilo_buy"][i] == True) & (df["macd_buy"][i] == False)) | (
    #             (df["hilo_buy"][i] == False) & (df["macd_buy"][i] == False)
    #         ):
    #             if flag != 0:
    #                 sigPriceBuy.append(np.NaN)
    #                 sigPriceSell.append(df["close"][i])
    #                 signal.append("sell")
    #                 flag = 0
    #             else:
    #                 sigPriceBuy.append(np.NaN)
    #                 sigPriceSell.append(np.NaN)
    #                 signal.append("neutral")
    #         else:
    #             sigPriceBuy.append(np.NaN)
    #             sigPriceSell.append(np.NaN)
    #             signal.append("neutral")

    #     return (sigPriceBuy, sigPriceSell, signal)
    
    # buy_sell = buy_sell(df)
    # print("buy-sell")    
    # print(df)












