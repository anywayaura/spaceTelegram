import logging
import os
import random
import time

import telebot

from service_functions import read_directory


def main():
    logging.basicConfig(level=logging.INFO)

    bot = telebot.TeleBot(os.getenv('SPACE_TELEGRAM_BOT_API_KEY'))
    chat_id = os.getenv('SPACE_TELEGRAM_CHAT_ID')
    image_list = []
    post_delay = int(os.getenv('SPACE_TELEGRAM_DELAY_HOURS', default=4)) * 3600

    def bot_post(chat_id, image_filename):
        with open(f'images{image_filename}', 'rb') as f:
            bot.send_photo(chat_id, f)

    while True:
        if not image_list:
            image_list = read_directory('images')
            if not image_list:
                logging.error('Image folder Empty, pleas fetch some pics.')
                break
        random.shuffle(image_list)
        filename = os.path.join('images', image_list.pop())
        with open(filename, 'rb') as f:
            bot.send_photo(chat_id, f)
        time.sleep(post_delay)

    # bot_post(chat_id, 'rhooph_tan_big.jpg')




if __name__ == '__main__':
    main()
