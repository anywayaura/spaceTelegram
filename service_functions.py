import os
from pathlib import Path
from urllib.parse import urlparse, unquote

import requests


def download_file(url, path):
    response = requests.get(url)
    response.raise_for_status()
    Path(path).mkdir(parents=True, exist_ok=True)
    filename = urlparse(unquote(url)).path.split('/')[-1]
    file_path = os.path.join(path, filename)

    with open(file=file_path, mode='wb') as f:
        f.write(response.content)


def get_extension(url):
    return os.path.splitext(url)[-1]


def read_directory(directory: str) -> list:
    return os.listdir(directory)


def main():
    download_file('https://wylsa.com/wp-content/uploads/2018/09/ffsdfsd.jpg#title?fycjers=wtf&idk=lol', 'images')


if __name__ == '__main__':
    main()
