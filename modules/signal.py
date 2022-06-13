# This file contains all the functions for providing signals to the user

# def signal_advice(collected_advices):
#     """This function gets the advice and uses it as input for the signalling
#     functions.
#     Args:
#         advice (string): The advice from the logic to send to the receiver
#     """
#     signal_field = ""
#     if collected_advices:
#         for advise in collected_advices:
#             signal = advise
#             signal_field += signal
#     # print(signal_field + "\nSignalling")
#     comms.telegram(signal_field)
#     # comms.pushbullet("CryptoMaven message", signal_field)
#     # comms.gmail("CryptoMaven message", signal_field)
