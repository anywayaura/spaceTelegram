import argparse
import logging

import requests

from service_functions import download_file


def fetch_spacex_latest():
    response = requests.get('https://api.spacexdata.com/v5/launches/latest')
    response.raise_for_status()

    for img in response.json()['links']['flickr_images']:
        download_file(img, 'images')


def fetch_spacex_by_id(id):
    response = requests.get(f'https://api.spacexdata.com/v5/launches/{id}')
    response.raise_for_status()

    for img in response.json()['links']['flickr']['original']:
        download_file(img, f'images')


def main():
    logging.basicConfig(level=logging.INFO)

    parser = argparse.ArgumentParser(description='Script downloads spacex latest or specified (-id <id>) flight photos')
    parser.add_argument('-id', help='id of the flight to fetch')
    args = parser.parse_args()

    try:
        if args.id:
            fetch_spacex_by_id(args.id)
        else:
            fetch_spacex_latest()
    except ConnectionError as ex:
        logging.error(f'Internet Problems: {ex}')
    except requests.exceptions.HTTPError:
        logging.error(f'What you are looking for cannot be found')
    except KeyError:
        logging.error(f'The flight has no photos')


if __name__ == '__main__':
    main()
