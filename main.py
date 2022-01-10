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
CRS20_ID = "5eb87d42ffd86e000604b384"


def get_image(url, dirname, filename):
    response = requests.get(url)
    response.raise_for_status()

    Path(dirname).mkdir(exist_ok=True)

    with open(f"{dirname}/{filename}", "wb") as file:
        file.write(response.content)


def get_spacex_links(launch_id: str) -> list:
    response = requests.get(
        f"{SPACEX_BASE_URL}{SPACEX_ENDPOINTS['all_launches']}/{launch_id}"
    )
    original_size_links = response.json()["links"]["flickr"]["original"]
    return original_size_links


def main():
    print(get_spacex_links(CRS20_ID))


if __name__ == "__main__":
    main()
