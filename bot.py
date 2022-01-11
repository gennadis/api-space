import os

import telegram
from dotenv import load_dotenv


def main():
    load_dotenv()
    tg_token = os.getenv("TELEGRAM_TOKEN")
    tg_channel = os.getenv("TELEGRAM_CHANNEL")

    bot = telegram.Bot(token=tg_token)

    # bot.send_message(chat_id=tg_channel, text="HELLO, WORLD!")
    with open("images/spacex1.jpg", "rb") as photo:
        bot.send_photo(chat_id=tg_channel, photo=photo)


if __name__ == "__main__":
    main()
