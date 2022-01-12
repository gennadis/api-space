import os

import telegram
from dotenv import load_dotenv

import config as conf
from bot import send_photos
from fetch_nasa import fetch_nasa_apod, fetch_nasa_epic
from fetch_spacex import fetch_spacex_launch


def main():
    """Download space images and start sending them to Telegram."""

    load_dotenv()
    nasa_token = os.getenv("NASA_TOKEN")

    fetch_spacex_launch(
        launch_id=conf.CRS20_ID,
        base_url=conf.SPACEX_BASE_URL,
        endpoint=conf.SPACEX_ENDPOINTS["all_launches"],
        dirname=conf.IMAGES_DIRNAME,
    )
    fetch_nasa_apod(
        token=nasa_token,
        base_url=conf.NASA_APOD_URL,
        dirname=conf.IMAGES_DIRNAME,
        count=30,
    )
    fetch_nasa_epic(
        token=nasa_token,
        base_url=conf.NASA_EPIC_URL,
        archive_url=conf.NASA_EPIC_ARCHIVE_URL,
        dirname=conf.IMAGES_DIRNAME,
    )

    bot = telegram.Bot(token=os.getenv("TELEGRAM_TOKEN"))
    while True:
        send_photos(
            bot=bot,
            dir_path=conf.IMAGES_DIRNAME,
            chat=os.getenv("TELEGRAM_CHANNEL"),
            delay=conf.SLEEP_DELAY,
        )


if __name__ == "__main__":
    main()
