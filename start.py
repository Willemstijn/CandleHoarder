# from matplotlib.pyplot import tick_params
import config
import functions
import secrets


def main():
    """For each symbol and each timeframe, 
    check if the database exists first and then 
    add the data to the database."""
    for symbol in config.symbols:
        for time_frame in config.time_frames:
            functions.check_db(symbol, time_frame)
            functions.fetch_base_data(symbol, time_frame)
            functions.last_full_candle(symbol, time_frame)


if __name__ == "__main__":
    main()
