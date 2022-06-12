# Import necessary libraries
import requests
import config
import json
import smtplib
from email.message import EmailMessage


def telegram(signal):
    """
    This function sends signals via Telegram
    See: https://python-telegram-bot.org/
    """
    # Enter your bot token and bot chat ID here for warnings with Telegram
    bot_token = config.token
    bot_chatID = config.chatID
    bot_message = signal
    send_text = (
        "https://api.telegram.org/bot"
        + bot_token
        + "/sendMessage?chat_id="
        + bot_chatID
        + "&parse_mode=Markdown&text="
        + bot_message
    )

    response = requests.get(send_text)
    return response.json()
    telegram_bot(bot_message)


def pushbullet(subject, signal):
    """Sending notification via pushbullet.
    From: https://simply-python.com/tag/pushbullet/
    Args:
        subject (str) : subject of text.
        body (str) : Body of text.
    """
    data_send = {"type": "note", "title": subject, "body": signal}

    ACCESS_TOKEN = config.pb_token
    resp = requests.post(
        "https://api.pushbullet.com/v2/pushes",
        data=json.dumps(data_send),
        headers={
            "Authorization": "Bearer " + ACCESS_TOKEN,
            "Content-Type": "application/json",
        },
    )
    if resp.status_code != 200:
        raise Exception("Something wrong with PushBullet")
    else:
        pass


def gmail(subject, signal):
    msg = EmailMessage()
    msg.set_content(signal)

    msg["Subject"] = subject
    msg["From"] = "CryptoMaven"
    msg["To"] = config.email_adressee

    # Send the message via our own SMTP server.
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(config.gmail_user, config.gmail_app_password)
    server.send_message(msg)
    server.quit()


def discord():
    # https://realpython.com/how-to-make-a-discord-bot-python/
    # https://www.devdungeon.com/content/make-discord-bot-python
    pass
