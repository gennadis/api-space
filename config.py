IMAGES_DIRNAME = "images"

SPACEX_BASE_URL = "https://api.spacexdata.com"
SPACEX_ENDPOINTS = {
    "latest": "/v4/launches/latest",
    "all_launches": "/v4/launches",
}

# As on Jan 11 2022, latest SpaceX launch has no images,
# hence using SpaceX CRS-20 launch ID
CRS20_ID = "5eb87d42ffd86e000604b384"

NASA_APOD_URL = "https://api.nasa.gov/planetary/apod"
NASA_EPIC_URL = "https://api.nasa.gov/EPIC/api/natural"
NASA_EPIC_ARCHIVE_URL = "https://api.nasa.gov/EPIC/archive/natural"

# Sleep in seconds
SLEEP_10_MINS = 600
SLEEP_24_HOURS = 86400
