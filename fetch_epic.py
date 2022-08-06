import logging

import requests

from service_functions import download_file


def get_epic():
    response = requests.get('http://epic.gsfc.nasa.gov/api/images.php')
    response.raise_for_status()

    for img in response.json():
        download_file(f'http://epic.gsfc.nasa.gov/epic-archive/jpg/{img["image"]}.jpg', 'images')


def main():
    logging.basicConfig(level=logging.INFO)
    try:
        get_epic()
    except ConnectionError as ex:
        logging.error(f'Internet Problems: {ex}')
    except requests.exceptions.HTTPError:
        logging.error(f'What you are looking for cannot be found')


if __name__ == '__main__':
    main()
