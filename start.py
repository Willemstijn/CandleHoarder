import config
import functions


def main():
    for symbol in config.symbols:
        for time_frame in config.time_frames:
            functions.check_db(symbol, time_frame)
            functions.fetch_data(symbol, time_frame)


if __name__ == "__main__":
    main()