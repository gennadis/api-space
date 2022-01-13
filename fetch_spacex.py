import requests

from utils import save_image


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
        save_image(url=link, dirname=dirname, filename=f"spacex{count}.jpg")


if __name__ == "__main__":
    pass
