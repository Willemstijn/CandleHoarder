# Import modules
import sys
from time import time
from config import *
from database import *
from candle import *

# Path to modules
sys.path.insert(1, "./modules/")

def main():
    """Walk throug the symbols and timeframes and create the databases and tables if necessary."""
    for symbol in symbols:
        for time_frame in time_frames:
            check_db(symbol, time_frame)
            is_entry = check_candle_data(symbol, time_frame)
            
            if is_entry:
                # if is_entry returns true (something other than 0), then start the download last candle function.
                # Else history will be downloaded with the download_candle_history function.
                download_last_candle(symbol, time_frame)
                print("Entry is: " + str(is_entry))


if __name__ == "__main__":
    main()
