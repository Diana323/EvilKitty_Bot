import telebot
from telebot import types

token = "6677943038:AAFthSBobYWh-QTjTTpNN3ygtq_X4LxfAIc"
bot = telebot.TeleBot("6677943038:AAFthSBobYWh-QTjTTpNN3ygtq_X4LxfAIc")

name = ""
surname = ""
age = 0


@bot.message_handler(commands=["start", "hello", "ПРИВІТ", ""])  # создаем команду
def start(message):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(
        "сайт",
        url="https://github.com/eternnoir/pyTelegramBotAPI/blob/master/examples/telebot_bot/telebot_bot.py",
    )
    markup.add(button1)
    bot.send_message(
        message.chat.id,
        "Привет,{0.first_name}! Нажми на кнопку замовити)".format(message.from_user),
        reply_markup=markup,
    )


@bot.message_handler(commands=["hello"])  # создаем команду
def start(message):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(
        "сайт",
        url="https://github.com/eternnoir/pyTelegramBotAPI/blob/master/examples/telebot_bot/telebot_bot.py",
    )
    markup.add(button1)
    bot.send_message(
        message.chat.id,
        "Привет,{0.first_name}!посмотреть товары)".format(message.from_user),
        reply_markup=markup,
    )


@bot.message_handler(content_types=["text"])
def func(message):
    if message.text == "Привет":
        bot.send_message(message.chat.id, text="Привет...👋 какой товар интересует❓)")
    elif message.text == "❓ Задать вопрос":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Смотреть товары")
        btn2 = types.KeyboardButton("оплата/доставка")
        btn3 = types.KeyboardButton("другой вопрос")
        back = types.KeyboardButton("главное меню")
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text="Задай мне вопрос", reply_markup=markup)

    elif message.text == "Смотреть товары":
        bot.send_message(message.chat.id, "Открыть каталог товаров")

    elif message.text == "оплата/доставка":
        bot.send_message(
            message.chat.id,
            text="lorem ipsum dolor? lorem ipsum dolor. lorem ipsum dolor,lorem ipsum dolor?lorem ipsum dolor",
        )
    elif message.text == "другой вопрос":
        bot.send_message(message.chat.id, "задайте вопрос, и я помогу")

    elif message.text == "главное меню":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Смотреть товары")
        button2 = types.KeyboardButton("оплата/доставка")
        markup.add(button1, button2)
        bot.send_message(
            message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup
        )
    else:
        bot.send_message(
            message.chat.id, text="На такую комманду я не запрограммировал.."
        )


@bot.message_handler(content_types=["text"])
def start(message):
    if message.text == "/reg":
        bot.send_message(message.from_user.id, "Как тебя зовут?")
        bot.register_next_step_handler(message, get_name)  # следующий шаг – get_name
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
        key_yes = types.InlineKeyboardButton(text="Да", callback_data="yes")
        keyboard.add(key_yes)  # добавляем кнопку в клавиатуру
        key_no = types.InlineKeyboardButton(text="Нет", callback_data="no")
        keyboard.add(key_no)
        question = "Тебе" + str(age) + " лет, тебя зовут " + name + " " + surname + "?"
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "yes":
        ...
        bot.send_message(call.message.chat.id, "Запомню : )")
    elif call.data == "no":
        ...  # переспрашиваем


bot.polling(none_stop=True, interval=0)
