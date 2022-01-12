# Space photos Telegram bot
This project was built for downloading some really nice space photos  
and publishing them to a Telegram channel.


## Features
- Download [SpaceX](https://www.flickr.com/photos/spacex/) launch pictures
- Download [NASA APOD](https://apod.nasa.gov/apod/astropix.html) pictures
- Download [NASA EPIC](https://epic.gsfc.nasa.gov/) pictures
- Publish photos repeatedly to a Telegram channel
- Set picture sending delay manually


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

4. Create .env file and fill it accordingly
```python
NASA_TOKEN=place_token_here
TELEGRAM_TOKEN=place_token_here
TELEGRAM_CHANNEL=@place_channel_name_here
```

5. Run
```bash
python main.py
```

## Tips:
- Don't forget to add your telegram bot to group admins!

- At `main.py` start, program will download around 50 pictures.  
It may take some time, so please be patient. And after that,  
telegram bot will start sending pictures to your group.

- Picture sending delay is 24 hours by default, but can be changed in `config.py`
