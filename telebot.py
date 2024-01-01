import os

import telebot

BOT_TOKEN = os.environ.get('6677943038:AAFthSBobYWh-QTjTTpNN3ygtq_X4LxfAIc')

bot = telebot.TeleBot(BOT_TOKEN)
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")
@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)