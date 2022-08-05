import logging

import telebot
import os

def main():
    logging.basicConfig(level=logging.DEBUG)

    bot = telebot.TeleBot(os.getenv('SPACE_TELEGRAM_BOT_API_KEY'))
    chat_id = os.getenv('SPACE_TELEGRAM_CHAT_ID')

    @bot.message_handler(commands=['start', 'help'])
    def send_welcome(message):
        bot.reply_to(message, "Howdy, how are you doing?")

    @bot.message_handler(commands=['post'])
    def post(message):
        bot.reply_to(message, 'Hei this is a post i sent to u xoxo')

    def bot_notify(chat_id, text):
        bot.send_message(chat_id, text)

    @bot.message_handler(func=lambda message: True)
    def echo_all(message):
        bot.reply_to(message, message.text)

    bot_notify(chat_id, 'I am running here ok?')

    bot.infinity_polling()
    
if __name__ == '__main__':
    main()
