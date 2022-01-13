import requests

from utils import save_image, parse_file_extension


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

        save_image(
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

        url = f"{archive_url}/{year}/{month}/{day}/png/{name}.png"
        save_image(
            url=url, params=params, dirname=dirname, filename=f"nasa_epic{count}.png"
        )


if __name__ == "__main__":
    pass
