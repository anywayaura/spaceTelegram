import logging
import os
import random
import time

import telebot
import requests
from dotenv import load_dotenv

from service_functions import read_directory


def main():
    load_dotenv()
    logging.basicConfig(level=logging.INFO)

    bot = telebot.TeleBot(os.environ['TG_BOT_API_KEY'])
    chat_id = os.environ['TG_CHAT_ID']
    image_list = []
    post_delay = int(os.getenv('TG_POST_DELAY', default=4)) * 3600

    while True:
        try:
            if not image_list:
                image_list = read_directory('images')
                if not image_list:
                    logging.error('Image folder Empty, please fetch some pics.')
                    break
            random.shuffle(image_list)
            filename = os.path.join('images', image_list.pop())
            with open(filename, 'rb') as f:
                bot.send_photo(chat_id, f)
            time.sleep(post_delay)
        except requests.exceptions.ConnectionError as _exce:
            logging.error(f'No internet connection ({_exce})')
            time.sleep(10)


if __name__ == '__main__':
    main()
