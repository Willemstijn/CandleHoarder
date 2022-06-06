# Import modules
import sys
from config import *
from modules.database import *
from modules.candle import *
from modules.dataframe import *

# Path to modules
sys.path.insert(1, "./modules/")

def main():
    """Walk throug the symbols and timeframes and create the databases and tables if necessary."""
    print("Starting to hoard...")
    for symbol in symbols:
        for time_frame in time_frames:
            # === THIS WHOLE SECTION BELOW IS COMMENTED OUT BUT IS GOOD!
            # check_db(symbol, time_frame)
            # is_entry = check_candle_data(symbol, time_frame)
            
            # if is_entry:
            #     # if is_entry returns true (something other than 0), then start the download last candle function.
            #     # Else history will be downloaded with the download_candle_history function.
            #     download_last_candle(symbol, time_frame, is_entry)
            # === THIS WHOLE SECTION ABOVE IS COMMENTED OUT BUT IS GOOD!    
            create_dataframe(symbol, time_frame)

if __name__ == "__main__":
    main()
