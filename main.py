import telebot

bot=telebot.TeleBot('6677943038:AAFthSBobYWh-QTjTTpNN3ygtq_X4LxfAIc')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, '<b>Привет</b>', parse_mode='html')

bot.polling(none_stop=True)
