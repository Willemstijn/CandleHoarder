##!/usr/bin/env python3
# This file contains all configurations for the hoarder.

from binance.client import Client
import secrets

# Installation directory.
dir = "/opt/CandleHoarder/"

# Enter the location where the databases should exist  be created.
data_location = "./data/"

# Enter the location for the plot export to the external wiki site plot directory
wiki = "/var/www/html/willemstijn.github.io/content/plots/"

# Select a timeframe to watch on.
# Available timeframes are: 1m, 3m, 5m, 15m, 30m, 1h, 2h, 4h, 6h, 8h, 12h, 1d, 3d, 1w, 1M.
time_frames = ["1d"]

# Candle lookback period for when fetching candle updates.
candle_lookback = 10

# Enter amount of historical data to fetch for initial candle data download.
candle_history = 2000

# Client key & secret for downloading data through the API exchange.
# See the secrets.py file for actual keys.
client = Client(secrets.BINANCE_API_KEY, secrets.BINANCE_API_SECRET)

symbols = ["BTCUSDT",
        "ETHUSDT",]
#         "BNBUSDT",
#         "SOLUSDT",
#         "ADAUSDT",
#         "XRPUSDT",
#         "LUNAUSDT",
#         "DOTUSDT",
#         "AVAXUSDT",
#         "DOGEUSDT",
#         "SHIBUSDT",
#         "MATICUSDT",
#         "ALGOUSDT",
#         "LTCUSDT",
#         "LINKUSDT",
#         "DAIUSDT",
#         "NEARUSDT",
#         "BCHUSDT",
#         "ATOMUSDT",
#         "TRXUSDT",
#         "XLMUSDT",
#         "FTMUSDT",
#         "MANAUSDT",
#         "AXSUSDT",
#         "HBARUSDT",
#         "VETUSDT",
#         "FTTUSDT",
#         "SANDUSDT",
#         "ICPUSDT",
#         "FILUSDT",
#         "THETAUSDT",
#         "EGLDUSDT",
#         "ETCUSDT",
#         "HNTUSDT",
#         "XMRUSDT",
#         "XTZUSDT",
#         "AAVEUSDT",
#         "KLAYUSDT",
#         "ONEUSDT",
#         "GRTUSDT",
#         "GALAUSDT",
#         "EOSUSDT",
#         "CAKEUSDT",
#         "STXUSDT",
#         "FLOWUSDT",
#         "BTTUSDT",
#         "LRCUSDT",
#         "CRVUSDT",
#         "KSMUSDT",
#         "MKRUSDT",
#         "ENJUSDT",
#         "QNTUSDT",
#         "XECUSDT",
#         "AMPUSDT",
#         "ZECUSDT",
#         "UNIUSDT",
#         "YFIUSDT",
#         "COMPUSDT",
#         "SUSHIUSDT",
# ]

# Enter all the crypto pairs you want to watch in this array.
# symbols = ["BTCUSDT", "ETHUSDT", "ADAUSDT", "XRPUSDT"]
# symbols = ["BTCUSDT"]
# symbols = [
#     # USDT quote
#     "1INCHUSDT","AAVEUSDT","ACAUSDT","ACHUSDT","ACMUSDT","ADAUSDT","ADADOWNUSDT","ADAUPUSDT","ADXUSDT","AGLDUSDT","AIONUSDT","AKROUSDT","ALCXUSDT","ALGOUSDT","ALICEUSDT","ALPACAUSDT","ALPHAUSDT","ALPINEUSDT","AMPUSDT","ANCUSDT","ANKRUSDT","ANTUSDT","APEUSDT","API3USDT","ARUSDT","ARDRUSDT","ARPAUSDT","ASRUSDT","ASTRUSDT","ATAUSDT","ATMUSDT","ATOMUSDT","AUCTIONUSDT","AUDUSDT","AUDIOUSDT","AUTOUSDT","AVAUSDT","AVAXUSDT","AXSUSDT","BADGERUSDT","BAKEUSDT","BALUSDT","BANDUSDT","BARUSDT","BATUSDT","BCHUSDT","BEAMUSDT","BELUSDT","BETAUSDT","BICOUSDT","BIFIUSDT","BLZUSDT","BNBUSDT","BNBDOWNUSDT","BNBUPUSDT","BNTUSDT","BNXUSDT","BONDUSDT","BSWUSDT","BTCUSDT","BTCDOWNUSDT","BTCSTUSDT","BTCUPUSDT","BTGUSDT","BTSUSDT","BTTCUSDT","BURGERUSDT","BUSDUSDT","C98USDT","CAKEUSDT","CELOUSDT","CELRUSDT","CFXUSDT","CHESSUSDT","CHRUSDT","CHZUSDT","CITYUSDT","CKBUSDT","CLVUSDT","COCOSUSDT","COMPUSDT","COSUSDT","COTIUSDT","CRVUSDT","CTKUSDT","CTSIUSDT","CTXCUSDT","CVCUSDT","CVPUSDT","CVXUSDT","DARUSDT","DASHUSDT","DATAUSDT","DCRUSDT","DEGOUSDT","DENTUSDT","DEXEUSDT","DFUSDT","DGBUSDT","DIAUSDT","DNTUSDT","DOCKUSDT","DODOUSDT","DOGEUSDT","DOTUSDT","DOTDOWNUSDT","DOTUPUSDT","DREPUSDT","DUSKUSDT","DYDXUSDT","EGLDUSDT","ELFUSDT","ENJUSDT","ENSUSDT","EOSUSDT","EPXUSDT","ERNUSDT","ETCUSDT","ETHUSDT","ETHDOWNUSDT","ETHUPUSDT","EURUSDT","FARMUSDT","FETUSDT","FIDAUSDT","FILUSDT","FIOUSDT","FIROUSDT","FISUSDT","FLMUSDT","FLOWUSDT","FLUXUSDT","FORUSDT","FORTHUSDT","FRONTUSDT","FTMUSDT","FTTUSDT","FUNUSDT","FXSUSDT","GALUSDT","GALAUSDT","GBPUSDT","GHSTUSDT","GLMRUSDT","GMTUSDT","GNOUSDT","GRTUSDT","GTCUSDT","GTOUSDT","HARDUSDT","HBARUSDT","HIGHUSDT","HIVEUSDT","HNTUSDT","HOTUSDT","ICPUSDT","ICXUSDT","IDEXUSDT","ILVUSDT","IMXUSDT","INJUSDT","IOSTUSDT","IOTAUSDT","IOTXUSDT","IRISUSDT","JASMYUSDT","JOEUSDT","JSTUSDT","JUVUSDT","KAVAUSDT","KDAUSDT","KEYUSDT","KLAYUSDT","KMDUSDT","KNCUSDT","KP3RUSDT","KSMUSDT","LAZIOUSDT","LDOUSDT","LINAUSDT","LINKUSDT","LINKDOWNUSDT","LINKUPUSDT","LITUSDT","LOKAUSDT","LPTUSDT","LRCUSDT","LSKUSDT","LTCUSDT","LTOUSDT","LUNAUSDT","MANAUSDT","MASKUSDT","MATICUSDT","MBLUSDT","MBOXUSDT","MCUSDT","MDTUSDT","MDXUSDT","MFTUSDT","MINAUSDT","MIRUSDT","MITHUSDT","MKRUSDT","MLNUSDT","MOBUSDT","MOVRUSDT","MTLUSDT","MULTIUSDT","NBSUSDT","NEARUSDT","NEOUSDT","NEXOUSDT","NKNUSDT","NMRUSDT","NULSUSDT","OCEANUSDT","OGUSDT","OGNUSDT","OMUSDT","OMGUSDT","ONEUSDT","ONGUSDT","ONTUSDT","OOKIUSDT","OPUSDT","ORNUSDT","OXTUSDT","PAXGUSDT","PEOPLEUSDT","PERLUSDT","PERPUSDT","PHAUSDT","PLAUSDT","PNTUSDT","POLSUSDT","POLYUSDT","PONDUSDT","PORTOUSDT","POWRUSDT","PSGUSDT","PUNDIXUSDT","PYRUSDT","QIUSDT","QNTUSDT","QTUMUSDT","QUICKUSDT","RADUSDT","RAMPUSDT","RAREUSDT","RAYUSDT","REEFUSDT","REIUSDT","RENUSDT","REPUSDT","REQUSDT","RIFUSDT","RLCUSDT","RNDRUSDT","ROSEUSDT","RSRUSDT","RUNEUSDT","RVNUSDT","SANDUSDT","SANTOSUSDT","SCUSDT","SCRTUSDT","SFPUSDT","SHIBUSDT","SKLUSDT","SLPUSDT","SNXUSDT","SOLUSDT","SPELLUSDT","SRMUSDT","STEEMUSDT","STMXUSDT","STORJUSDT","STPTUSDT","STRAXUSDT","STXUSDT","SUNUSDT","SUPERUSDT","SUSHIUSDT","SXPUSDT","SYSUSDT","TUSDT","TCTUSDT","TFUELUSDT","THETAUSDT","TKOUSDT","TLMUSDT","TOMOUSDT","TORNUSDT","TRBUSDT","TRIBEUSDT","TROYUSDT","TRUUSDT","TRXUSDT","TRXDOWNUSDT","TRXUPUSDT","TUSDUSDT","TVKUSDT","TWTUSDT","UMAUSDT","UNFIUSDT","UNIUSDT","USDCUSDT","USDPUSDT","UTKUSDT","VETUSDT","VGXUSDT","VIDTUSDT","VITEUSDT","VOXELUSDT","VTHOUSDT","WANUSDT","WAVESUSDT","WAXPUSDT","WINUSDT","WINGUSDT","WNXMUSDT","WOOUSDT","WRXUSDT","WTCUSDT","XECUSDT","XEMUSDT","XLMUSDT","XMRUSDT","XNOUSDT","XRPUSDT","XRPDOWNUSDT","XRPUPUSDT","XTZUSDT","XVGUSDT","XVSUSDT","YFIUSDT","YFIIUSDT","YGGUSDT","ZECUSDT","ZENUSDT","ZILUSDT","ZRXUSDT",
#     # BTC quote
#     "1INCHBTC","AAVEBTC","ACABTC","ACHBTC","ACMBTC","ADABTC","ADXBTC","AERGOBTC","AGIXBTC","AGLDBTC","AIONBTC","ALCXBTC","ALGOBTC","ALICEBTC","ALPACABTC","ALPHABTC","ALPINEBTC","AMBBTC","AMPBTC","ANCBTC","ANKRBTC","ANTBTC","APEBTC","API3BTC","ARBTC","ARDRBTC","ARKBTC","ARPABTC","ASRBTC","ASTBTC","ASTRBTC","ATABTC","ATMBTC","ATOMBTC","AUCTIONBTC","AUDIOBTC","AUTOBTC","AVABTC","AVAXBTC","AXSBTC","BADGERBTC","BAKEBTC","BALBTC","BANDBTC","BARBTC","BATBTC","BCHBTC","BEAMBTC","BELBTC","BETABTC","BICOBTC","BLZBTC","BNBBTC","BNTBTC","BNXBTC","BONDBTC","BRDBTC","BTCSTBTC","BTGBTC","BTSBTC","C98BTC","CAKEBTC","CELOBTC","CELRBTC","CFXBTC","CHESSBTC","CHRBTC","CHZBTC","CITYBTC","CLVBTC","COMPBTC","COSBTC","COTIBTC","CRVBTC","CTKBTC","CTSIBTC","CTXCBTC","CVCBTC","CVXBTC","DARBTC","DASHBTC","DATABTC","DCRBTC","DEGOBTC","DGBBTC","DIABTC","DNTBTC","DOCKBTC","DODOBTC","DOGEBTC","DOTBTC","DREPBTC","DUSKBTC","DYDXBTC","EGLDBTC","ELFBTC","ENJBTC","ENSBTC","EOSBTC","ETCBTC","ETHBTC","EZBTC","FARMBTC","FETBTC","FIDABTC","FILBTC","FIOBTC","FIROBTC","FISBTC","FLMBTC","FLOWBTC","FLUXBTC","FORBTC","FORTHBTC","FRONTBTC","FTMBTC","FTTBTC","FXSBTC","GALBTC","GALABTC","GASBTC","GLMBTC","GLMRBTC","GMTBTC","GNOBTC","GOBTC","GRSBTC","GRTBTC","GTCBTC","GTOBTC","HARDBTC","HBARBTC","HIGHBTC","HIVEBTC","HNTBTC","ICPBTC","ICXBTC","IDEXBTC","ILVBTC","IMXBTC","INJBTC","IOSTBTC","IOTABTC","IOTXBTC","IRISBTC","JASMYBTC","JOEBTC","JSTBTC","JUVBTC","KAVABTC","KDABTC","KLAYBTC","KMDBTC","KNCBTC","KSMBTC","LAZIOBTC","LDOBTC","LINABTC","LINKBTC","LITBTC","LOKABTC","LOOMBTC","LPTBTC","LRCBTC","LSKBTC","LTCBTC","LTOBTC","MANABTC","MATICBTC","MBOXBTC","MCBTC","MDABTC","MDTBTC","MDXBTC","MINABTC","MIRBTC","MITHBTC","MKRBTC","MLNBTC","MOBBTC","MOVRBTC","MTLBTC","MULTIBTC","NASBTC","NAVBTC","NEARBTC","NEBLBTC","NEOBTC","NEXOBTC","NKNBTC","NMRBTC","NULSBTC","NXSBTC","OAXBTC","OCEANBTC","OGBTC","OGNBTC","OMBTC","OMGBTC","ONEBTC","ONGBTC","ONTBTC","OPBTC","ORNBTC","OXTBTC","PAXGBTC","PEOPLEBTC","PERLBTC","PERPBTC","PHABTC","PHBBTC","PIVXBTC","PLABTC","PNTBTC","POLSBTC","POLYBTC","PONDBTC","PORTOBTC","POWRBTC","PROMBTC","PSGBTC","PYRBTC","QIBTC","QKCBTC","QLCBTC","QNTBTC","QSPBTC","QTUMBTC","QUICKBTC","RADBTC","RAMPBTC","RAREBTC","RENBTC","REPBTC","REQBTC","RIFBTC","RLCBTC","RNDRBTC","ROSEBTC","RUNEBTC","RVNBTC","SANDBTC","SANTOSBTC","SCBTC","SCRTBTC","SFPBTC","SKLBTC","SNMBTC","SNTBTC","SNXBTC","SOLBTC","SRMBTC","SSVBTC","STEEMBTC","STMXBTC","STORJBTC","STPTBTC","STRAXBTC","STXBTC","SUPERBTC","SUSHIBTC","SXPBTC","SYSBTC","TCTBTC","TFUELBTC","THETABTC","TKOBTC","TLMBTC","TOMOBTC","TORNBTC","TRBBTC","TRIBEBTC","TRUBTC","TRXBTC","TVKBTC","TWTBTC","UMABTC","UNFIBTC","UNIBTC","UTKBTC","VETBTC","VGXBTC","VIBBTC","VIDTBTC","VITEBTC","VOXELBTC","WABIBTC","WANBTC","WAVESBTC","WAXPBTC","WBTCBTC","WINGBTC","WOOBTC","WRXBTC","WTCBTC","XEMBTC","XLMBTC","XMRBTC","XNOBTC","XRPBTC","XTZBTC","XVGBTC","XVSBTC","YFIBTC","YFIIBTC","YGGBTC","ZECBTC","ZENBTC","ZILBTC","ZRXBTC"
# ]
