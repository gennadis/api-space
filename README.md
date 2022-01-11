# Space photos donwloader

This project was built for downloading some really nice space photos.

## Features
- Download [SpaceX](https://www.flickr.com/photos/spacex/) launch photos
- Download [NASA APOD](https://apod.nasa.gov/apod/astropix.html) pictures
- Download [NASA EPIC](https://epic.gsfc.nasa.gov/) pictures.


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

4. Create .env file and place your NASA Open API Token in it
```python
NASA_TOKEN=place_your_token_here
```

5. Run
```bash
python main.py
```
