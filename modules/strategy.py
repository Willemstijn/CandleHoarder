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

    # Determine lookback period.
    days = 500

    # Create colums in dataframe for plotting.
    df['sma21'] = pta.sma(df["close"], length=21)
    df['ema21'] = pta.ema(df["close"], length=21)

    # Plot output to graphs for wiki.
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

    # Create log chart.
    # plt.yscale('log')

    plt.gcf().autofmt_xdate()

    # Plot buy / sell signals.
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


def moving_averages(symbol, time_frame, df):
    """
    A collection of important moving averages in this chart. Be aware that each of them can act as support
    and/or resistance.
    """

    print(f"Creating moving averages plot for {symbol} on {time_frame}...")

    if len(df) > 998:
        # Determine lookback period.
        days = 500

        # Calculate moving averages.
        df['sma21'] = pta.sma(df["close"], length=21)
        df['ema21'] = pta.ema(df["close"], length=21)
        df['sma50'] = pta.sma(df["close"], length=50)
        df['sma100'] = pta.sma(df["close"], length=100)
        df['sma200'] = pta.sma(df["close"], length=200)
        df['wsma20'] = pta.sma(df["close"], length=140)
        # df['wsma200'] = pta.sma(df["close"], length=1400)

        # Plot output to graphs for wiki.
        plt.style.use('seaborn-notebook')
        plt.figure(figsize=(14, 7))
        plt.grid(linestyle='--', linewidth=0.3)

        # df.sort_values(df['Date'], inplace=True)

        dates = df['openTime'].tail(days)
        price = df['close'].tail(days)
        sma21 = df['sma21'].tail(days)
        sma50 = df['sma50'].tail(days)
        sma100 = df['sma100'].tail(days)
        sma200 = df['sma200'].tail(days)
        wsma20 = df['wsma20'].tail(days)
        # wsma200 = df['wsma200'].tail(days)

        # Adding lines.
        plt.plot(dates, price, label='Price', linewidth=3, color='blue')
        plt.plot(dates, sma21, label='21 sma daily', linewidth=1, color='red')
        plt.plot(dates, sma50, label='50 sma daily', linewidth=1, color='orange')
        plt.plot(dates, sma100, label='100 sma daily', linewidth=1, color='yellow')
        plt.plot(dates, sma200, label='200 sma daily', linewidth=1, color='green')
        plt.plot(dates, wsma20, label='20 sma weekly', linewidth=1, color='purple')
        # plt.plot(dates, wsma200, label='200 sma weekly (absolute bottom?)', linewidth=1, color='black')

        # Create log chart.
        # plt.yscale('log')

        plt.gcf().autofmt_xdate()

        plt.title(symbol + ' moving averages - ' + ct)
        plt.xlabel('Date')
        plt.ylabel('Price (log)')
        plt.legend(loc='upper left')

        plt.tight_layout()
        plt.savefig(f'{dir}/plots/averages-{symbol}-{time_frame}.png')
        plt.cla()
        plt.close()
    elif len(df) < 998:
        print(symbol + ' has not enough data to create moving averages chart')


def supertrend(symbol, time_frame, df):
    """
    Plot of supertrend indicator with macd and rsi.
    """

    print(f"Creating Supertrend plot for {symbol} on {time_frame}...")

    # Determine lookback period
    days = 500

    # Calculate supertrend indicator
    # supertrend
    length = 5
    multiplier = 3.6
    df["supertrend"] = pta.supertrend(high=df["high"],low=df["low"],close=df["close"],length=length,multiplier=multiplier,)[f"SUPERT_{length}_{multiplier}"]

    # macd
    fast = 12
    slow = 26
    smooth = 9
    df["macd"] = pta.macd(close=df["close"], fast=fast, slow=slow, signal=smooth, offset=None)[f"MACD_{fast}_{slow}_{smooth}"]
    df["macds"] = pta.macd(close=df["close"], fast=fast, slow=slow, signal=smooth, offset=None)[f"MACDs_{fast}_{slow}_{smooth}"]
    # df["macdh"] = pta.macd(close=df["close"], fast=fast, slow=slow, signal=smooth, offset=None)[f"MACDh_{fast}_{slow}_{smooth}"]

    # rsi
    df["rsi"] = pta.rsi(close=df["close"], timeperiod=14)

    # Plot output to graphs for wiki.
    plt.style.use('seaborn-notebook')
    plt.figure(figsize=(14, 7))
    plt.grid(linestyle='--', linewidth=0.3)

    # df.sort_values(df['Date'], inplace=True)

    dates = df['openTime'].tail(days)
    price = df['close'].tail(days)
    supertrend = df["supertrend"].tail(days)
    macd = df['macd'].tail(days)
    macdsignal = df['macds'].tail(days)
    rsi = df["rsi"].tail(days)
    
    # Adding lines to upper plot.
    plt.subplot(3, 1, 1)
    plt.plot(dates, price, label='Price', linewidth=3)
    plt.plot(dates, supertrend, label='SuperTrend', linewidth=1, color='green', alpha=1)

    # Chart markup
    plt.title(symbol + ' Supertrend  - ' + ct)
    plt.xlabel('Date')
    plt.ylabel('Price in USD')
    plt.legend(loc='upper left')
    plt.tight_layout()
    plt.grid(linestyle='--')

    # Adding lines to middle plot.
    plt.subplot(3, 1, 2)
    plt.plot(dates, macd, label='macd', linewidth=1, color='red', alpha=1)
    plt.plot(dates, macdsignal, label='signal', linewidth=1, color='blue', alpha=1)
    plt.axhline(y=0, color='grey', linestyle='--', linewidth=2)
    plt.xlabel('Date')
    plt.ylabel('macd')

    # Adding lines to lower plot.
    plt.subplot(3, 1, 3)
    plt.plot(dates, rsi, label='rsi', linewidth=1, color='purple', alpha=1)
    plt.axhline(y=50, color='grey', linestyle='--', linewidth=2)
    plt.axhline(y=30, color='grey', linestyle='--', linewidth=1)
    plt.axhline(y=70, color='grey', linestyle='--', linewidth=1)
    plt.xlabel('Date')
    plt.ylabel('rsi')

    plt.gcf().autofmt_xdate()

    # plt.suptitle(symbol + ' Chart')

    # Plot to file
    plt.savefig(f'{dir}/plots/supertrend-{symbol}-{time_frame}.png')
    plt.cla()
    plt.close()

