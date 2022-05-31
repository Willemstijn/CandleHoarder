# Import modules
from time import time
from config import *
from database import *
from candle import *


def main():
    """Walk throug the symbols and timeframes and create the databases and tables if necessary."""
    for symbol in symbols:
        for time_frame in time_frames:
            check_db(symbol, time_frame)
            check_candle_data(symbol, time_frame)
            # download_last_candle(symbol, time_frame)


if __name__ == "__main__":
    main()
