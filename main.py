import telebot
from telebot import types
token=''
bot = telebot.TeleBot("6677943038:AAFthSBobYWh-QTjTTpNN3ygtq_X4LxfAIc")

name = ''
surname =''
age = 0
@bot.message_handler(commands=["start"])
def start(message):
        mess = f"Привет, <b>{message.from_user.first_name}</b>"
        bot.send_message(message.chat.id, mess, parse_mode="html")

@bot.message_handler(content_types=["text"])
def start(message):
    if message.text == "/reg":
        bot.send_message(message.from_user.id, "Как тебя зовут?", parse_mode="html")
        bot.register_next_step_handler(
            message, get_name)  # следующий шаг – функция get_name
    else:
        bot.send_message(message.from_user.id, "Напиши /reg")

def get_name(message):  # получаем фамилию
    global name
    name = message.text
    bot.send_message(message.from_user.id, "Какая у тебя фамилия?")
    bot.register_next_step_handler(message, get_surname)

def get_surname(message):
    global surname
    surname = message.text
    bot.send_message(message.from_user.id, "Сколько тебе лет?")
    bot.register_next_step_handler(message, get_age)

def get_age(message):
    global age
    while age == 0:
        try:
            age = int(message.text)  # проверяем, что возраст введен корректно
        except Exception:
            bot.send_message(message.from_user.id, "Цифрами, пожалуйста")
        keyboard = types.InlineKeyboardMarkup()
        key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
        keyboard.add(key_yes) #добавляем кнопку в клавиатуру
        key_no = types.InlineKeyboardButton(text='Нет', callback_data='no')
        keyboard.add(key_no)
        question = 'Тебе'+str(age)+' лет, тебя зовут '+name+' '+surname+'?'
    bot.send_message(
        message.from_user.id,
        "Тебе " + str(age) + " лет, тебя зовут " + name + " " + surname + "?",)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "yes":
        ...
        bot.send_message(call.message.chat.id, "Запомню :)")
    elif call.data == "no":
        ...  # переспрашиваем


bot.polling(none_stop=True)