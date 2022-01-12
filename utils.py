import os
import pathlib
import requests
import urllib


def get_image(url: str, dirname: str, filename: str) -> None:
    """Download and save image from URL given."""

    response = requests.get(url)
    response.raise_for_status()

    pathlib.Path(dirname).mkdir(exist_ok=True)

    with open(f"{dirname}/{filename}", "wb") as file:
        file.write(response.content)


def parse_file_extension(url: str) -> str:
    """Get file extension from URL given."""

    parsed_url = urllib.parse.urlsplit(url)
    root, extension = os.path.splitext(parsed_url.path)
    return extension


if __name__ == "__main__":
    pass