import requests


def get_image(filename, url):
    response = requests.get(url)
    response.raise_for_status()

    with open(filename, "wb") as file:
        file.write(response.content)


def main():
    filename = "hubble.jpeg"
    url = "https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg"
    get_image(filename, url)


if __name__ == "__main__":
    main()
