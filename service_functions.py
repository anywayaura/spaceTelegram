import os
from pathlib import Path

import requests


def download_file(url, path):
    response = requests.get(url)
    response.raise_for_status()
    Path(path).mkdir(parents=True, exist_ok=True)
    file_path = os.path.join(path, url.split('/')[-1])

    with open(file=file_path, mode='wb') as f:
        f.write(response.content)


def get_extension(url):
    return os.path.splitext(url)[-1]


def read_directory(directory: str) -> list:
    return os.listdir(directory)


def main():
    pass


if __name__ == '__main__':
    main()
