# Space photos donwloader

This project was built for downloading some really nice space photos
and publishing them to a Telegram channel.

## Features
- Download [SpaceX](https://www.flickr.com/photos/spacex/) launch photos
- Download [NASA APOD](https://apod.nasa.gov/apod/astropix.html) pictures
- Download [NASA EPIC](https://epic.gsfc.nasa.gov/) pictures
- Publish photos repeatedly to a Telegram channel
- Change photos sending delay

## Installation notes
1. Clone project
```bash
git clone https://github.com/gennadis/api-space.git
cd api-space
```

2. Create and activate virtual environment
```bash
python3 -m venv env
source env/bin/activate
```

3. Install requirements
```bash
pip install -r requirements.txt
```

4. Create .env file and place your Tokens in it
```python
NASA_TOKEN=place_your_token_here
TELEGRAM_TOKEN=place_your_token_here
TELEGRAM_CHANNEL=@place_your_channel_name_here
```

5. Run
```bash
python main.py
```

6. Check created ```images``` folder for downloaded photos!

7. Photos sending delay is 24 Hours by default, but it can be changed in ```config.py```.