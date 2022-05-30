# What is CandleHoarder

CandleHoarder is a program to fetch (or hoards) Cryptocurrency pairs information (a.k.a.candles) from the Binance exchange and puts them into a database for further local analysis. The SQLite database with candle information can be used for analysis with tools as Jupyter notebooks or other scripts that depend on the OHLVC information of a Crypto pair.

## How it works

The program works as follows:

1. Check the information in the config.py file to see which pairs and which timeframes should be hoarded
2. Check if a database already exists, if not then:
    * Create the database and table of the pair and timeframe
    * Download the history of candles for that pair
3. At regular intervals, download the latest candle
    * If candles are missing, download these
4. If database already exists, then see step 3.

# Installation and configuration requirements

## Installation

Create virtual environment:

```
# Install Python virtualenv software
pip3 install virtualenv

# Change to directory and create a virtual environment
cd CandleHoarder
virtualenv venv
source venv/bin/activate

# Install packages for CandleHoarder
pip install -r requirements.txt
```

## Configuration

## secret file

File 'secret.py' should be made to contain confidential information. The format should be:

```
api_key = ""
api_secret = ""

```

This file is not here by default but should be made manually.

## Misc

Read: 

* https://python-binance.readthedocs.io/en/latest/overview.html
* https://python-binance.readthedocs.io/en/latest/constants.html

For information about the python-binance library.


