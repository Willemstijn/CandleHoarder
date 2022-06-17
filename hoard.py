#!/usr/bin/python
# coding=utf-8

# Import modules.
import sys
import logging
from config import *
from modules.database import *
from modules.candle import *
from modules.dataframe import *
from modules.strategy import *
from modules.sync import *
from modules.pages import create_pages

# Path to CandleHoarder specific modules.
sys.path.insert(1, "./modules/")

def main():
    """Walk throug the symbols and timeframes and create the databases and tables if necessary."""
    logging.warning("Starting hoarding of candles...")
    for symbol in symbols:
        for time_frame in time_frames:
            # === THIS WHOLE SECTION BELOW IS COMMENTED OUT BUT IS GOOD!
            logging.warning("Checking " + symbol + " on " + time_frame + ".")
            check_db(symbol, time_frame)
            is_entry = check_candle_data(symbol, time_frame)
            
            if is_entry:
                # if is_entry returns true (something other than 0), then start the download last candle function.
                # Else history will be downloaded with the download_candle_history function.
                download_last_candle(symbol, time_frame, is_entry)
            # === THIS WHOLE SECTION ABOVE IS COMMENTED OUT BUT IS GOOD!

            # Create dataframe of each symbol for further analysis.
            df = create_dataframe(symbol, time_frame)
            
            # Define the strategies you want to test in the section below:
            mayer_multiple(symbol, time_frame, df)
            bull_support_band(symbol, time_frame, df)
            moving_averages(symbol, time_frame, df)
            supertrend(symbol, time_frame, df)
            pi_cycle(symbol, time_frame, df)
    
    # Create the markdown pages with the links to the plots (Special function for dynamic pairs lists)
    create_pages()

    # Synchronise the plots and pages that were created by the strategy to an external wiki site for publishing.
    sync_plots()
    sync_pages()

logging.warning("End of hoarding, everything seemed succesfull...")

if __name__ == "__main__":
    main()
