import requests
from pathlib import Path


def get_image(url, dirname, filename):
    response = requests.get(url)
    response.raise_for_status()

    Path(dirname).mkdir(exist_ok=True)

    with open(f"{dirname}/{filename}", "wb") as file:
        file.write(response.content)


def main():
    dirname = "images"
    filename = "hubble.jpeg"
    url = "https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg"
    get_image(url, dirname, filename)


if __name__ == "__main__":
    main()
