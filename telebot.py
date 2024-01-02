#import os

#import telebot

#BOT_TOKEN = os.environ.get('6677943038:AAFthSBobYWh-QTjTTpNN3ygtq_X4LxfAIc')

#bot = telebot.TeleBot(BOT_TOKEN)
#@bot.message_handler(commands=['start', 'hello'])
#def send_welcome(message):
#    bot.reply_to(message, "Howdy, how are you doing?")
#@bot.message_handler(func=lambda msg: True)
#def echo_all(message):
#    bot.reply_to(message, message.text)
import telebot
bot=telebot.TeleBot('6677943038:AAFthSBobYWh-QTjTTpNN3ygtq_X4LxfAIc')

@bot.message_handlers(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'привет, для заказа товара нажмите <a>заказать</a>', parse_mode='html')
    bot.polling(none_stop=True)