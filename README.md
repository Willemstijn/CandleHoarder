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

# in windows:  source venv/Scripts/activate

# Install packages for CandleHoarder
pip install -r requirements.txt
```

## Configuration

## secret file

File 'secret.py' should be made to contain confidential information. The content of the file should be at least:

```
BINANCE_API_KEY = ""
BINANCE_API_SECRET = ""

```

This file is not here by default but should be made manually.

## Packages

This program uses the following packages:

* python-binance (https://pypi.org/project/python-binance/)
* schedule (https://pypi.org/project/schedule/)
* 
## Misc

Read: 

* https://python-binance.readthedocs.io/en/latest/overview.html
* https://python-binance.readthedocs.io/en/latest/constants.html

For information about the python-binance library.

## Getting markets

At this moment I use the Freqtrade 'list-markets' option to fetch all `Binance` information to fill my configuration file with trading pair information. At the moment I use two specific commands to get USDT and BTC base pair information:

```
freqtrade list-markets --userdir /opt/freqtrade/user_data/  --config user_data/backtest-config.json --exchange binance --print-json --quote USDT


freqtrade list-markets --userdir /opt/freqtrade/user_data/  --config user_data/backtest-config.json --exchange binance --print-json --quote BTC
```

Results of the queries above are:

```
symbols = [
    # USDT quote
    "1INCHUSDT","AAVEUSDT","ACAUSDT","ACHUSDT","ACMUSDT","ADAUSDT","ADADOWNUSDT","ADAUPUSDT","ADXUSDT","AGLDUSDT","AIONUSDT","AKROUSDT","ALCXUSDT","ALGOUSDT","ALICEUSDT","ALPACAUSDT","ALPHAUSDT","ALPINEUSDT","AMPUSDT","ANCUSDT","ANKRUSDT","ANTUSDT","APEUSDT","API3USDT","ARUSDT","ARDRUSDT","ARPAUSDT","ASRUSDT","ASTRUSDT","ATAUSDT","ATMUSDT","ATOMUSDT","AUCTIONUSDT","AUDUSDT","AUDIOUSDT","AUTOUSDT","AVAUSDT","AVAXUSDT","AXSUSDT","BADGERUSDT","BAKEUSDT","BALUSDT","BANDUSDT","BARUSDT","BATUSDT","BCHUSDT","BEAMUSDT","BELUSDT","BETAUSDT","BICOUSDT","BIFIUSDT","BLZUSDT","BNBUSDT","BNBDOWNUSDT","BNBUPUSDT","BNTUSDT","BNXUSDT","BONDUSDT","BSWUSDT","BTCUSDT","BTCDOWNUSDT","BTCSTUSDT","BTCUPUSDT","BTGUSDT","BTSUSDT","BTTCUSDT","BURGERUSDT","BUSDUSDT","C98USDT","CAKEUSDT","CELOUSDT","CELRUSDT","CFXUSDT","CHESSUSDT","CHRUSDT","CHZUSDT","CITYUSDT","CKBUSDT","CLVUSDT","COCOSUSDT","COMPUSDT","COSUSDT","COTIUSDT","CRVUSDT","CTKUSDT","CTSIUSDT","CTXCUSDT","CVCUSDT","CVPUSDT","CVXUSDT","DARUSDT","DASHUSDT","DATAUSDT","DCRUSDT","DEGOUSDT","DENTUSDT","DEXEUSDT","DFUSDT","DGBUSDT","DIAUSDT","DNTUSDT","DOCKUSDT","DODOUSDT","DOGEUSDT","DOTUSDT","DOTDOWNUSDT","DOTUPUSDT","DREPUSDT","DUSKUSDT","DYDXUSDT","EGLDUSDT","ELFUSDT","ENJUSDT","ENSUSDT","EOSUSDT","EPXUSDT","ERNUSDT","ETCUSDT","ETHUSDT","ETHDOWNUSDT","ETHUPUSDT","EURUSDT","FARMUSDT","FETUSDT","FIDAUSDT","FILUSDT","FIOUSDT","FIROUSDT","FISUSDT","FLMUSDT","FLOWUSDT","FLUXUSDT","FORUSDT","FORTHUSDT","FRONTUSDT","FTMUSDT","FTTUSDT","FUNUSDT","FXSUSDT","GALUSDT","GALAUSDT","GBPUSDT","GHSTUSDT","GLMRUSDT","GMTUSDT","GNOUSDT","GRTUSDT","GTCUSDT","GTOUSDT","HARDUSDT","HBARUSDT","HIGHUSDT","HIVEUSDT","HNTUSDT","HOTUSDT","ICPUSDT","ICXUSDT","IDEXUSDT","ILVUSDT","IMXUSDT","INJUSDT","IOSTUSDT","IOTAUSDT","IOTXUSDT","IRISUSDT","JASMYUSDT","JOEUSDT","JSTUSDT","JUVUSDT","KAVAUSDT","KDAUSDT","KEYUSDT","KLAYUSDT","KMDUSDT","KNCUSDT","KP3RUSDT","KSMUSDT","LAZIOUSDT","LDOUSDT","LINAUSDT","LINKUSDT","LINKDOWNUSDT","LINKUPUSDT","LITUSDT","LOKAUSDT","LPTUSDT","LRCUSDT","LSKUSDT","LTCUSDT","LTOUSDT","LUNAUSDT","MANAUSDT","MASKUSDT","MATICUSDT","MBLUSDT","MBOXUSDT","MCUSDT","MDTUSDT","MDXUSDT","MFTUSDT","MINAUSDT","MIRUSDT","MITHUSDT","MKRUSDT","MLNUSDT","MOBUSDT","MOVRUSDT","MTLUSDT","MULTIUSDT","NBSUSDT","NEARUSDT","NEOUSDT","NEXOUSDT","NKNUSDT","NMRUSDT","NULSUSDT","OCEANUSDT","OGUSDT","OGNUSDT","OMUSDT","OMGUSDT","ONEUSDT","ONGUSDT","ONTUSDT","OOKIUSDT","OPUSDT","ORNUSDT","OXTUSDT","PAXGUSDT","PEOPLEUSDT","PERLUSDT","PERPUSDT","PHAUSDT","PLAUSDT","PNTUSDT","POLSUSDT","POLYUSDT","PONDUSDT","PORTOUSDT","POWRUSDT","PSGUSDT","PUNDIXUSDT","PYRUSDT","QIUSDT","QNTUSDT","QTUMUSDT","QUICKUSDT","RADUSDT","RAMPUSDT","RAREUSDT","RAYUSDT","REEFUSDT","REIUSDT","RENUSDT","REPUSDT","REQUSDT","RIFUSDT","RLCUSDT","RNDRUSDT","ROSEUSDT","RSRUSDT","RUNEUSDT","RVNUSDT","SANDUSDT","SANTOSUSDT","SCUSDT","SCRTUSDT","SFPUSDT","SHIBUSDT","SKLUSDT","SLPUSDT","SNXUSDT","SOLUSDT","SPELLUSDT","SRMUSDT","STEEMUSDT","STMXUSDT","STORJUSDT","STPTUSDT","STRAXUSDT","STXUSDT","SUNUSDT","SUPERUSDT","SUSHIUSDT","SXPUSDT","SYSUSDT","TUSDT","TCTUSDT","TFUELUSDT","THETAUSDT","TKOUSDT","TLMUSDT","TOMOUSDT","TORNUSDT","TRBUSDT","TRIBEUSDT","TROYUSDT","TRUUSDT","TRXUSDT","TRXDOWNUSDT","TRXUPUSDT","TUSDUSDT","TVKUSDT","TWTUSDT","UMAUSDT","UNFIUSDT","UNIUSDT","USDCUSDT","USDPUSDT","UTKUSDT","VETUSDT","VGXUSDT","VIDTUSDT","VITEUSDT","VOXELUSDT","VTHOUSDT","WANUSDT","WAVESUSDT","WAXPUSDT","WINUSDT","WINGUSDT","WNXMUSDT","WOOUSDT","WRXUSDT","WTCUSDT","XECUSDT","XEMUSDT","XLMUSDT","XMRUSDT","XNOUSDT","XRPUSDT","XRPDOWNUSDT","XRPUPUSDT","XTZUSDT","XVGUSDT","XVSUSDT","YFIUSDT","YFIIUSDT","YGGUSDT","ZECUSDT","ZENUSDT","ZILUSDT","ZRXUSDT",
    # BTC quote
    "1INCHBTC","AAVEBTC","ACABTC","ACHBTC","ACMBTC","ADABTC","ADXBTC","AERGOBTC","AGIXBTC","AGLDBTC","AIONBTC","ALCXBTC","ALGOBTC","ALICEBTC","ALPACABTC","ALPHABTC","ALPINEBTC","AMBBTC","AMPBTC","ANCBTC","ANKRBTC","ANTBTC","APEBTC","API3BTC","ARBTC","ARDRBTC","ARKBTC","ARPABTC","ASRBTC","ASTBTC","ASTRBTC","ATABTC","ATMBTC","ATOMBTC","AUCTIONBTC","AUDIOBTC","AUTOBTC","AVABTC","AVAXBTC","AXSBTC","BADGERBTC","BAKEBTC","BALBTC","BANDBTC","BARBTC","BATBTC","BCHBTC","BEAMBTC","BELBTC","BETABTC","BICOBTC","BLZBTC","BNBBTC","BNTBTC","BNXBTC","BONDBTC","BRDBTC","BTCSTBTC","BTGBTC","BTSBTC","C98BTC","CAKEBTC","CELOBTC","CELRBTC","CFXBTC","CHESSBTC","CHRBTC","CHZBTC","CITYBTC","CLVBTC","COMPBTC","COSBTC","COTIBTC","CRVBTC","CTKBTC","CTSIBTC","CTXCBTC","CVCBTC","CVXBTC","DARBTC","DASHBTC","DATABTC","DCRBTC","DEGOBTC","DGBBTC","DIABTC","DNTBTC","DOCKBTC","DODOBTC","DOGEBTC","DOTBTC","DREPBTC","DUSKBTC","DYDXBTC","EGLDBTC","ELFBTC","ENJBTC","ENSBTC","EOSBTC","ETCBTC","ETHBTC","EZBTC","FARMBTC","FETBTC","FIDABTC","FILBTC","FIOBTC","FIROBTC","FISBTC","FLMBTC","FLOWBTC","FLUXBTC","FORBTC","FORTHBTC","FRONTBTC","FTMBTC","FTTBTC","FXSBTC","GALBTC","GALABTC","GASBTC","GLMBTC","GLMRBTC","GMTBTC","GNOBTC","GOBTC","GRSBTC","GRTBTC","GTCBTC","GTOBTC","HARDBTC","HBARBTC","HIGHBTC","HIVEBTC","HNTBTC","ICPBTC","ICXBTC","IDEXBTC","ILVBTC","IMXBTC","INJBTC","IOSTBTC","IOTABTC","IOTXBTC","IRISBTC","JASMYBTC","JOEBTC","JSTBTC","JUVBTC","KAVABTC","KDABTC","KLAYBTC","KMDBTC","KNCBTC","KSMBTC","LAZIOBTC","LDOBTC","LINABTC","LINKBTC","LITBTC","LOKABTC","LOOMBTC","LPTBTC","LRCBTC","LSKBTC","LTCBTC","LTOBTC","MANABTC","MATICBTC","MBOXBTC","MCBTC","MDABTC","MDTBTC","MDXBTC","MINABTC","MIRBTC","MITHBTC","MKRBTC","MLNBTC","MOBBTC","MOVRBTC","MTLBTC","MULTIBTC","NASBTC","NAVBTC","NEARBTC","NEBLBTC","NEOBTC","NEXOBTC","NKNBTC","NMRBTC","NULSBTC","NXSBTC","OAXBTC","OCEANBTC","OGBTC","OGNBTC","OMBTC","OMGBTC","ONEBTC","ONGBTC","ONTBTC","OPBTC","ORNBTC","OXTBTC","PAXGBTC","PEOPLEBTC","PERLBTC","PERPBTC","PHABTC","PHBBTC","PIVXBTC","PLABTC","PNTBTC","POLSBTC","POLYBTC","PONDBTC","PORTOBTC","POWRBTC","PROMBTC","PSGBTC","PYRBTC","QIBTC","QKCBTC","QLCBTC","QNTBTC","QSPBTC","QTUMBTC","QUICKBTC","RADBTC","RAMPBTC","RAREBTC","RENBTC","REPBTC","REQBTC","RIFBTC","RLCBTC","RNDRBTC","ROSEBTC","RUNEBTC","RVNBTC","SANDBTC","SANTOSBTC","SCBTC","SCRTBTC","SFPBTC","SKLBTC","SNMBTC","SNTBTC","SNXBTC","SOLBTC","SRMBTC","SSVBTC","STEEMBTC","STMXBTC","STORJBTC","STPTBTC","STRAXBTC","STXBTC","SUPERBTC","SUSHIBTC","SXPBTC","SYSBTC","TCTBTC","TFUELBTC","THETABTC","TKOBTC","TLMBTC","TOMOBTC","TORNBTC","TRBBTC","TRIBEBTC","TRUBTC","TRXBTC","TVKBTC","TWTBTC","UMABTC","UNFIBTC","UNIBTC","UTKBTC","VETBTC","VGXBTC","VIBBTC","VIDTBTC","VITEBTC","VOXELBTC","WABIBTC","WANBTC","WAVESBTC","WAXPBTC","WBTCBTC","WINGBTC","WOOBTC","WRXBTC","WTCBTC","XEMBTC","XLMBTC","XMRBTC","XNOBTC","XRPBTC","XTZBTC","XVGBTC","XVSBTC","YFIBTC","YFIIBTC","YGGBTC","ZECBTC","ZENBTC","ZILBTC","ZRXBTC"
]

```

The top 50 pairs according to Coinmarketcap contains the following USDT crypto pairs. I keep this here as a reference...

```
symbols = ["BTCUSDT",
        "ETHUSDT",
        "BNBUSDT",
        "SOLUSDT",
        "ADAUSDT",
        "XRPUSDT",
        "LUNAUSDT",
        "DOTUSDT",
        "AVAXUSDT",
        "DOGEUSDT",
        "SHIBUSDT",
        "MATICUSDT",
        "ALGOUSDT",
        "LTCUSDT",
        "LINKUSDT",
        "DAIUSDT",
        "NEARUSDT",
        "BCHUSDT",
        "ATOMUSDT",
        "TRXUSDT",
        "XLMUSDT",
        "FTMUSDT",
        "MANAUSDT",
        "AXSUSDT",
        "HBARUSDT",
        "VETUSDT",
        "FTTUSDT",
        "SANDUSDT",
        "ICPUSDT",
        "FILUSDT",
        "THETAUSDT",
        "EGLDUSDT",
        "ETCUSDT",
        "HNTUSDT",
        "XMRUSDT",
        "XTZUSDT",
        "AAVEUSDT",
        "KLAYUSDT",
        "ONEUSDT",
        "GRTUSDT",
        "GALAUSDT",
        "EOSUSDT",
        "CAKEUSDT",
        "STXUSDT",
        "FLOWUSDT",
        "BTTUSDT",
        "LRCUSDT",
        "CRVUSDT",
        "KSMUSDT",
        "MKRUSDT",
        "ENJUSDT",
        "QNTUSDT",
        "XECUSDT",
        "AMPUSDT",
        "ZECUSDT",
        "UNIUSDT",
        "YFIUSDT",
        "COMPUSDT",
        "SUSHIUSDT",
]
```