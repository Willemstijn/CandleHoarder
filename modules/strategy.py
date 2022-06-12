# This file contains all the strategies that will be calculated and plotted.
from distutils.command.config import config
import imp
import pandas as pd
import pandas_ta as pta
import ta as ta
import numpy as np
from config import dir as dir
from datetime import datetime, timedelta
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates

# ct stores current time.
ct = str(datetime.now())

def test(symbol, time_frame, df):
    print(symbol, time_frame)
    print(df)


def mayer_multiple(symbol, time_frame, df):
    """
    Introduced by Trace Mayer as a way to gauge the current price of Bitcoin against its long range 
    historical price movements (200 day moving average), the Mayer Multiple highlights when Bitcoin 
    is overbought or oversold in the context of longer time frames.

    Mayer Multiple Formula:
    
    Bitcoin market price / 200 day MA value = Mayer Multiple

    Any multiple above the 2.4 threshold has historically shown to signify the beginning of a 
    speculative bubble, which is significant because all bubbles eventually burst, causing a rapid 
    depreciation. 

    The Mayer Multiple has never fallen below 0.237, the value that marked the bottom of bitcoin’s 
    first significant bear market in 2011.

    Any value above 2.4 means that your assets should be (DCA) sold because of bullish overextension 
    to the SMA200 and FOMO. Here you lock in profits. Any value below 0.7 means that assets could be 
    (DCA) bought because of bearish overextention and FUD in the markets. Here you buy when blood runs
    though the streets.
    """

    print(f"Creating Mayer multiple plot for {symbol} on {time_frame}...")

    if len(df) > 201:
        # Determine lookback period.
        days = 500
        upper_band_factor = 2.4
        lower_band_factor = 0.7
        
        # Create additional colums in dataframe for plotting and calculating Mayer multiple.
        # First create sma200 and then divide close price with sma200 to get Mayer multiple.
        df['sma200'] = (pta.sma(df["close"], length=200)).round(2)
        df["mayer"] = (df["close"] / df['sma200']).round(2)
        df["upper_band_factor"] = upper_band_factor
        df["lower_band_factor"] = lower_band_factor

        # Plot output to graphs for wiki.
        plt.style.use('seaborn-notebook')
        plt.figure(figsize=(14, 7))
        plt.grid(linestyle='--', linewidth=0.3)

        dates = df['openTime'].tail(days)
        upper_band = df["upper_band_factor"].tail(days)
        lower_band = df["lower_band_factor"].tail(days)
        mayer = df['mayer'].tail(days)

        # Adding lines.
        plt.plot(dates, upper_band, label='DCA out band', linewidth=1, color='red')
        plt.plot(dates, mayer, label='Mayer multiple factor', linewidth=3, color='blue')
        plt.plot(dates, lower_band, label='DCA in band', linewidth=1, color='green')

        plt.gcf().autofmt_xdate()

        # Fill when mayer goes above/below bands.
        plt.fill_between(dates, upper_band, mayer,where=(mayer > upper_band), color='red', alpha=0.25,label='DCA sell')
        plt.fill_between(dates, lower_band, mayer,where=(mayer < lower_band), color='green', alpha=0.25,label='DCA buy')
        
        plt.title(symbol + ' Mayer multiple - ' + ct)
        plt.xlabel('Date')
        plt.ylabel('Mayer factor')
        plt.legend(loc='upper left')

        plt.tight_layout()
        plt.savefig(f'{dir}plots/mayer-{symbol}-{time_frame}.png')
        plt.cla()
        plt.close()
    elif len(df) < 201:
        print(symbol + ' has not enough data to create Mayer multiple chart')

    # TODO: create an export of the Mayer result for each pair and enter it into the database for creating a buy/sell overview of all the 
    # TODO: indicators later in the process.


def bull_support_band(symbol, time_frame, df):
    """
    The bull support band is a band consisting of the 21 sma and 21 ema. When the close price is above both the
    sma and ema, and ema is above sma, then a bullish market can be formed. As long as the price is below or around
    the band, there is no clear direction.
    """

    print(f"Creating Bull support band plot for {symbol} on {time_frame}...")

    # Determine lookback period
    days = 500

    # Create colums in dataframe for plotting
    df['sma21'] = pta.sma(df["close"], length=21)
    df['ema21'] = pta.ema(df["close"], length=21)

    # Plot output to graphs for wiki
    plt.style.use('seaborn-notebook')
    plt.figure(figsize=(14, 7))
    plt.grid(linestyle='--', linewidth=0.3)

    # df.sort_values(df['Date'], inplace=True)

    dates = df['openTime'].tail(days)
    price = df['close'].tail(days)
    sma21 = df['sma21'].tail(days)
    ema21 = df['ema21'].tail(days)

    # Adding lines
    plt.plot(dates, price, label='Price', linewidth=3, color='blue')
    plt.plot(dates, ema21, label='21 ema daily', linewidth=1, color='red')
    plt.plot(dates, sma21, label='21 sma daily', linewidth=1, color='green')

    # Create log chart
    # plt.yscale('log')

    plt.gcf().autofmt_xdate()

    # Plot buy / sell signals
    plt.fill_between(dates, ema21, sma21,where=(ema21 >= sma21), color='green', alpha=0.25,label='Bullish')
    plt.fill_between(dates, ema21, sma21,where=(ema21 <= sma21), color='red', alpha=0.25,label='Bearish')

    plt.title(symbol + ' 21ema / 21sma bull support band - ' + ct)
    plt.xlabel('Date')
    plt.ylabel('Price (log)')
    plt.legend(loc='upper left')

    plt.tight_layout()
    plt.savefig(f'{dir}plots/bullsupport-{symbol}-{time_frame}.png')
    plt.cla()
    plt.close()
