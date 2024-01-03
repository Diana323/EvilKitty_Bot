import main
bot=main.TeleBot('6677943038:AAFthSBobYWh-QTjTTpNN3ygtq_X4LxfAIc')

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'привет, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')

bot.polling(none_stop=True)