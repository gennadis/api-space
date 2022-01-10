import requests
from pathlib import Path

IMAGES_DIRNAME = "images"
SPACEX_BASE_URL = "https://api.spacexdata.com"
SPACEX_ENDPOINTS = {
    "latest": "/v4/launches/latest",
    "all_launches": "/v4/launches",
}

# latest launch has no images,
# hence using custom launch ID
# https://en.wikipedia.org/wiki/SpaceX_CRS-20
CRS20_ID = "5eb87d42ffd86e000604b384"


def get_image(url, dirname, filename):
    response = requests.get(url)
    response.raise_for_status()

    Path(dirname).mkdir(exist_ok=True)

    with open(f"{dirname}/{filename}", "wb") as file:
        file.write(response.content)


def fetch_spacex_launch(launch_id: str):
    response = requests.get(
        f"{SPACEX_BASE_URL}{SPACEX_ENDPOINTS['all_launches']}/{launch_id}"
    )
    response.raise_for_status()
    original_size_links = response.json()["links"]["flickr"]["original"]
    for count, link in enumerate(original_size_links, start=1):
        get_image(url=link, dirname=IMAGES_DIRNAME, filename=f"spacex{count}.jpg")


def main():
    fetch_spacex_launch(CRS20_ID)


if __name__ == "__main__":
    main()
