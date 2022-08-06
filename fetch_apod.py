import logging
import os

import requests

from service_functions import download_file


def get_nasa_apod(api_key, count=10):
    params = {
        'api_key': api_key,
        'count': count
    }
    response = requests.get('https://api.nasa.gov/planetary/apod', params)
    response.raise_for_status()

    for apod in response.json():
        download_file(apod.get('hdurl', 'url'), 'images')


def main():
    logging.basicConfig(level=logging.INFO)
    try:
        get_nasa_apod(os.environ['NASA_API_KEY'])
    except ConnectionError as ex:
        logging.error(f'Internet Problems: {ex}')
    except requests.exceptions.HTTPError:
        logging.error(f'What you are looking for cannot be found')


if __name__ == '__main__':
    main()
