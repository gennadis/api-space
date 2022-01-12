# Image settings
IMAGES_DIRNAME = "images"


# SpaceX API settings
SPACEX_BASE_URL = "https://api.spacexdata.com"
SPACEX_ENDPOINTS = {
    "latest": "/v4/launches/latest",
    "all_launches": "/v4/launches",
}
CRS20_ID = "5eb87d42ffd86e000604b384"
# As on Jan 11 2022, latest SpaceX launch has no images,
# hence using SpaceX CRS-20 launch ID


# NASA Open API settings
NASA_APOD_URL = "https://api.nasa.gov/planetary/apod"
NASA_EPIC_URL = "https://api.nasa.gov/EPIC/api/natural"
NASA_EPIC_ARCHIVE_URL = "https://api.nasa.gov/EPIC/archive/natural"


# Telegram bot settings
SLEEP_DELAY = 86400  # 24 hours in seconds
