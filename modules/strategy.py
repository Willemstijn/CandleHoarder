# This file contains all the strategies that will be calculated and plotted

# def check_swing_strategy(symbol, timeframe, df):
#     """Function that checks the last candle close and returns signals when a
#     change in advice is detected."""

#     # Get the second to last entry in the dataframe column with advice
#     # This is the last full closing day.
#     change = df.iloc[-2]["POS_adv_changed"]
#     advice = df.iloc[-2]["POS_adv"]
#     close = df.iloc[-2]["close"].round(2)

#     # If change field is false (not the same as the previous advice),
#     # then the advice has been changed and a warning should be created.
#     if change == False:
#         # return swing strategy advice
#         signal_field = "{} signal {} ({}).\nClose: {},\n\n".format(
#             advice, symbol, timeframe, close
#         )
#         return signal_field