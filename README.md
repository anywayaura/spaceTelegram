# spaceTelegram

###### The script to post photos to telegram group over time delay, also downloading capabilities provided

_using the list of apis:_

- SPACEX launches
- EPIC Earth Polychromatic Imaging Camera
- Nasa Astronomy Picture of the Day


### space_telegram.py:

###### Posts images from images folder

_setup env variables:_

`SPACE_TELEGRAM_BOT_API_KEY` - your telegram bot api

`SPACE_TELEGRAM_CHAT_ID` - chat id u want to post images (bot have to be administrator of this group)

`SPACE_TELEGRAM_DELAY_HOURS` - how often (hrs)

```
python space_telegram.py
```

### fetch_apod.py:

###### Downloads some NASA astronomy picture of the day to the images folder

_setup env variable:_

`NASA_API_KEY` - get urself a key here: https://api.nasa.gov

_usage example:_
```
python fetch_apod.py
```

### fetch_spacex.py:

###### Downloads spaceX launch photos to images folder

_usage examples:_

- _fetch specified launch by id:_
```
python fetch_spacex.py -id '5eb87d47ffd86e000604b38a'
```
- _fetch latest launch (have in mind: not every launch has photos)_
```
python fetch_spacex.py
```

### fetch_epic.py

###### Downloads Earth Polychromatic Imaging Camera to images folder

_usage example:_

```
python fetch_epic.py
```
__________________________________________________________________

**Requirement libraries based in `requirements.txt`**

```
pip install -r requirements.txt
```