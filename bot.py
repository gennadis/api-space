import os
from time import sleep

import telegram
from dotenv import load_dotenv

import config as conf


def send_photos(bot, dir_path: str, chat: str, delay: int):
    """Send photos from given ditectory to Telegram chat."""

    for filename in os.listdir(dir_path):
        if filename.endswith((".jpg", ".gif", ".png")):
            bot.send_photo(chat_id=chat, photo=open(f"{dir_path}/{filename}", "rb"))

            sleep(delay)


def main():
    load_dotenv()
    bot = telegram.Bot(token=os.getenv("TELEGRAM_TOKEN"))

    while True:
        send_photos(
            bot=bot,
            dir_path=conf.IMAGES_DIRNAME,
            chat=os.getenv("TELEGRAM_CHANNEL"),
            delay=conf.SLEEP_24_HOURS,
        )


if __name__ == "__main__":
    main()
