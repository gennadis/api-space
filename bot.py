import os
from time import sleep


def send_photos(bot, dir_path: str, chat: str, delay: int):
    """Send photos from given ditectory to Telegram chat."""

    for filename in os.listdir(dir_path):
        if filename.endswith((".jpg", ".gif", ".png")):
            with open(f"{dir_path}/{filename}", "rb") as photo:
                bot.send_photo(chat_id=chat, photo=photo)

            sleep(delay)
