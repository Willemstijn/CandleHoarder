# This file contains all the strategies that will be calculated and plotted
import pandas as pd
import pandas_ta as pta
import ta as ta
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates

def test(symbol, time_frame, df):
    print(symbol, time_frame)
    print(df)

def mayer_multiple(df):
    upper_band_factor = 2.4
    lower_band_factor = 0.7
    df['sma200'] = (pta.sma(df["close"], length=200)).round(2)
    df["u"] = (df["close"] / df['sma200']).round(2)

    # Old way of calculating Mayer multiple for plot against price graph
    # df['sma200'] = pta.sma(df["close"], length=200)
    # df['mayer'] = (pta.sma(df["close"], length=200) * 2.4)

        # Plot output to graphs for wiki
        plt.style.use('seaborn-notebook')
        plt.figure(figsize=(14, 7))
        plt.grid(linestyle='--', linewidth=1)

        # df.sort_values(df['Date'], inplace=True)

        dates = df['# openTime'].tail(days)
        price = df['close'].tail(days)
        mayer = df['mayer'].tail(days)
        sma = df['sma200'].tail(days)

        # Adding lines
        plt.plot(dates, price, label='Price')
        plt.plot(dates, mayer, label='Mayer multiple')
        plt.plot(dates, sma, label='200 sma daily')

        # Create log chart
        plt.yscale('log')

        plt.gcf().autofmt_xdate()

        # Fill when price goes above/below MA's
        # Fill the area between the py_salaries line and the dev_salaries line
        # give different colors in each area
        plt.fill_between(dates, price, mayer, where=(price >= mayer), color='red', alpha=0.25, label='DCA sell')
        # plt.fill_between(dates, price, y2lowsma,
        #                  where=(price <= y2lowsma), color='green', alpha=0.25,
        #                 label='DCA buy')

        plt.title(symbol + ' Mayer multiple - ' + ct)
        plt.xlabel('Date')
        plt.ylabel('Price (log)')
        plt.legend(loc='upper left')

        plt.tight_layout()
        plt.savefig(f'{cfg.dir}/plots/mayer-{symbol}-{timeframe}.png')
        plt.cla()
        plt.close()
    elif len(df) < 200:
        print(symbol + ' has not enough data to create Mayer multiple chart')

    print(df)

