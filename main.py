import os
import pathlib
import requests
import urllib

from dotenv import load_dotenv

import config as conf


def get_image(url: str, dirname: str, filename: str) -> None:
    """Download and save image from URL given."""

    response = requests.get(url)
    response.raise_for_status()

    pathlib.Path(dirname).mkdir(exist_ok=True)

    with open(f"{dirname}/{filename}", "wb") as file:
        file.write(response.content)


def fetch_spacex_launch(
    launch_id: str,
    base_url: str,
    endpoint: str,
    dirname: str,
) -> None:
    """
    Download SpaceX launch photos of launch ID given.
    https://github.com/r-spacex/SpaceX-API

    """

    response = requests.get(f"{base_url}{endpoint}/{launch_id}")
    response.raise_for_status()

    original_size_links: list = response.json()["links"]["flickr"]["original"]

    for count, link in enumerate(original_size_links, start=1):
        get_image(url=link, dirname=dirname, filename=f"spacex{count}.jpg")


def parse_file_extension(url: str) -> str:
    """Get file extension from URL given."""

    parsed_url = urllib.parse.urlsplit(url)
    root, extension = os.path.splitext(parsed_url.path)
    return extension


def fetch_nasa_apod(token: str, base_url: str, dirname: str, count: int) -> None:
    """
    Download 'count' amount of NASA APOD pictures.
    https://github.com/nasa/apod-api

    """

    params = {
        "api_key": token,
        "thumbs": True,  # get thumbnail if media is video
        "count": count,
    }
    response = requests.get(url=base_url, params=params)
    response.raise_for_status()

    astro_pictures = response.json()

    for count, picture in enumerate(astro_pictures, start=1):
        if picture.get("media_type") == "image":
            url = picture.get("url")
        elif picture.get("media_type") == "video":
            url = picture.get("thumbnail_url")  # videos "url" is youtube link

        get_image(
            url=url,
            dirname=dirname,
            filename=f"nasa_apod{count}{parse_file_extension(url)}",
        )


def fetch_nasa_epic(token: str, base_url: str, archive_url: str, dirname: str) -> None:
    """
    Download NASA EPIC pictures.
    https://epic.gsfc.nasa.gov/about/api

    """

    params = {
        "api_key": token,
    }
    response = requests.get(url=base_url, params=params)
    response.raise_for_status()

    earth_pictures = response.json()

    for count, picture in enumerate(earth_pictures, start=1):
        name = picture.get("image")
        date, time = picture.get("date").split()
        year, month, day = date.split("-")

        url = f"{archive_url}/{year}/{month}/{day}/png/{name}.png?api_key={token}"
        get_image(url=url, dirname=dirname, filename=f"nasa_epic{count}.png")


def main():
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


if __name__ == "__main__":
    main()
