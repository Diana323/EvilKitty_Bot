import telebot

bot = telebot.TeleBot("6677943038:AAFthSBobYWh-QTjTTpNN3ygtq_X4LxfAIc")

@bot.message_handler(commands=["start"])
def start(message):
    mess = f"Привет, <b>{message.from_user.first_name}</b>"
    bot.send_message(message.chat.id, mess, parse_mode="html")

@bot.message_handler()
def get_user_text(message):
    bot.send_message(message.chat.id, message, parse_mode="html")

bot.polling(none_stop=True)
