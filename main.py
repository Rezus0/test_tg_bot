import random
import telebot
from telebot import types


bot = telebot.TeleBot("##############")  # создание бота


@bot.message_handler(commands=['start'])  # обработка команды /start
def start_command(message):
    bot.send_message(message.from_user.id, greetings)


@bot.message_handler(commands=['help'])  # обработка команды /help
def help_command(message):
    bot.send_message(message.from_user.id, helptext + "\n\n" + helptext2 + "\n\n" + helptext3 + "\n\n" + helptext4)


@bot.message_handler(commands=['reg'])  # обработка команды /reg
def registration(message):
    bot.send_message(message.from_user.id, "Ваше имя:")
    bot.register_next_step_handler(message, get_name)


@bot.message_handler(commands=['documents'])  # вывод URL-кнопки и информации о подаче документов + вывод картинки
def documents(message):
    markup = types.InlineKeyboardMarkup()
    docs_button = types.InlineKeyboardButton(text="Как подать документы", url="https://rut-miit.ru/admissions"
                                                                              "/office/48052")
    markup.add(docs_button)
    bot.send_photo(message.from_user.id, open("files/documents.png", "rb"), "Нажмите на кнопку, чтобы узнать как "
                                                                            "подать документы в РУТ(МИИТ)",
                   reply_markup=markup)


@bot.message_handler(commands=['account'])  # обработка команды /account
def account(message):
    if name != "" and surname != "" and surname != "" and age != 0:
        if age % 10 == 1 and age % 100 != 11:
            bot.send_message(message.from_user.id, surname + " " + name + " " + middlename + ".\n" + str(age) + " год.")
        elif (age % 10 == 2 or age % 10 == 3 or age % 10 == 4) and age % 100 != 12 and age % 100 != 13 and age % 100 \
                != 14:
            bot.send_message(message.from_user.id,
                             surname + " " + name + " " + middlename + ".\n" + str(age) + " года.")
        else:
            bot.send_message(message.from_user.id, surname + " " + name + " " + middlename + ".\n" + str(age) + " лет.")
    else:
        bot.send_message(message.from_user.id, "Вы не зарегистрированы! Используйте /reg")


@bot.message_handler(commands=['sticker'])  # создание callback-кнопок
def sticker_sender(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("Веселые😀", callback_data="funny")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Грустные☹️", callback_data="sad")
    )
    bot.send_message(message.from_user.id, "Выбери из какой категории хочешь получить стикер", reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)  # реакция на callback-кнопки (отправка стикеров)
def callback(query):
    data = query.data
    bot.edit_message_reply_markup(query.from_user.id, query.message.message_id)
    if data == "funny":
        bot.send_sticker(query.from_user.id, random.choice(funnystickers))
    elif data == "sad":
        bot.send_sticker(query.from_user.id, random.choice(sadstickers))


@bot.message_handler(content_types="text")  # реакция на сообщения вне функций
def get_text_messages(message):
    if message.text.lower() == "привет":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    elif message.text.lower() == "как подать документы?":
        documents(message)
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю, пока только учу человеческий😞" + "\n" +
                         "Используй /help, чтобы узнать, что я умею.")


greetings = "Доброго времени суток, данный бот создан для тестирования функций, но скоро тут будет много интересного, " \
            "используй /help, чтобы узнать, что бот умеет."
helptext = "Хочешь получить рандомный стикер из выбранной катергории? Используй /sticker"
helptext2 = "Хочешь зарегистрироваться? Используй /reg"
helptext3 = "Уже зарегистрирован? Получи информацию о своем аккаунте командой /account"
helptext4 = "Хочешь узнать, как подать документы в РУТ(МИИТ)? Используй /documents"
name = ""
surname = ""
middlename = ""
age = 0
funnystickers = ["CAACAgIAAxkBAAEDP1hhis_cjI09T0OFsijv-fTPD-R8xwACFgADwDZPE2Ah1y2iBLZnIgQ",
                 "CAACAgIAAxkBAAEDP1phis_1JHdopkMzEgYe-DhGIy8E0gACbwEAAuB5UgeYDk7MrXDi7yIE",
                 "CAACAgIAAxkBAAEDP1xhitAMpKsPyvuW35jXImZ9pltxuQACHQEAAjDUnRGhYZw-05wbTyIE",
                 "CAACAgIAAxkBAAEDP15hitAnMb6g75Hpe-F_NWCkTvQ3fQACNAADr8ZRGr2WC4V16TqzIgQ",
                 "CAACAgIAAxkBAAEDP2BhitA4UnaNhXY7TRUx6A4aGi5r-wACDAADkP2aFZ9oJ0jCaOrRIgQ",
                 "CAACAgIAAxkBAAEDP2JhitBZXQABSRnv90t-gzZfZ9Rk8s4AAlgAA8A2TxP92B9p4gJXuyIE"
                 ]
sadstickers = ["CAACAgQAAxkBAAEDP2RhitB0LRhD5hQpXRIGgxp_gs3fxAACJBAAAswdmwzFk26zIhbF_yIE",
               "CAACAgIAAxkBAAEDP2lhitCeqU1CVEo15rPoEa6olV6sDAACRw4AAhFwoUqPrBZNBIPa2yIE",
               "CAACAgIAAxkBAAEDP2phitCr_hFaJyhH1CeILSa-8vQY5QACUwMAAuB5UgfYeklgfRKsiCIE",
               "CAACAgIAAxkBAAEDP3BhitDxUOFRhsTzEhbdSx0ow_ys0gACUw8AAkcG-EsYhXwrKl3SnCIE",
               "CAACAgIAAxkBAAEDP3JhitECpJoXGy56A6XRhgmlej-9kQAC3gADMNSdEYG5ydbBAytAIgQ",
               "CAACAgQAAxkBAAEDP3RhitEJoRWmgUZWMBDLRfB6A1ED6AACYhEAAswdmwytUMTpt2oDkSIE"
               ]


def get_name(message):  # получение имени
    global name
    name = message.text
    if name.isnumeric():
        bot.send_message(message.from_user.id, "Введите данные корректно, пожалуйста.")
        bot.register_next_step_handler(message, get_name)
    else:
        bot.send_message(message.from_user.id, "Ваша фамилия:")
        bot.register_next_step_handler(message, get_surname)


def get_surname(message):  # получение фамилии
    global surname
    surname = message.text
    if surname.isnumeric():
        bot.send_message(message.from_user.id, "Введите данные корректно, пожалуйста.")
        bot.register_next_step_handler(message, get_surname)
    else:
        bot.send_message(message.from_user.id, "Ваше отчество:")
        bot.register_next_step_handler(message, get_middlename)


def get_middlename(message):  # получение отчества
    global middlename
    middlename = message.text
    if middlename.isnumeric():
        bot.send_message(message.from_user.id, "Введите данные корректно, пожалуйста.")
        bot.register_next_step_handler(message, get_middlename)
    else:
        bot.send_message(message.from_user.id, "Ваш возраст:")
        bot.register_next_step_handler(message, get_age)


def get_age(message):  # получение возраста до тех пор, пока не будет введен цифрами
    global age
    try:
        if 0 < int(message.text) < 200:
            age = int(message.text)
            check_information(message)
        else:
            bot.send_message(message.from_user.id, "Введите корректный возраст, пожалуйста.")
            bot.register_next_step_handler(message, get_age)
    except Exception:
        bot.send_message(message.from_user.id, "Цифрами, пожалуйста.")
        bot.register_next_step_handler(message, get_age)


def check_information(message):  # создание кнопок на клавиатуре в телеграме, вызов функции на реакцию на кнопку
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_yes = types.KeyboardButton("Да")
    item_no = types.KeyboardButton("Нет")
    markup.add(item_yes)
    markup.add(item_no)
    if age % 10 == 1 and age % 100 != 11:
        bot.send_message(message.from_user.id, surname + " " + name + " " + middlename + ".\n" + str(
            age) + " год." + "\n\n" + "Информация корректна?", reply_markup=markup)
    elif (age % 10 == 2 or age % 10 == 3 or age % 10 == 4) and age % 100 != 12 and age % 100 != 13 and age % 100 != 14:
        bot.send_message(message.from_user.id, surname + " " + name + " " + middlename + ".\n" + str(
            age) + " года." + "\n\n" + "Информация корректна?", reply_markup=markup)
    else:
        bot.send_message(message.from_user.id, surname + " " + name + " " + middlename + ".\n" + str(
            age) + " лет." + "\n\n" + "Информация корректна?", reply_markup=markup)
    bot.register_next_step_handler(message, check_reaction)


@bot.message_handler(content_types="text")  # реакция на текст с кнопок из предыдущей функции
def check_reaction(message):
    if message.text.lower() == "да":
        bot.send_message(message.from_user.id, "Все отлично!", reply_markup=types.ReplyKeyboardRemove(),
                         parse_mode="Markdown")
    elif message.text.lower() == "нет":
        bot.send_message(message.from_user.id, "Используйте /reg, чтобы повторно пройти регистрацию.",
                         reply_markup=types.ReplyKeyboardRemove(), parse_mode="Markdown")
@bot.message_handler(commands=['achievements'])
def achievements_command(message):
    markup = types.InlineKeyboardMarkup()
    ach_button = types.InlineKeyboardButton(text="Индивидуальные достижения", url="https://www.miit.ru/admissions/office/136668")
    markup.add(ach_button)
    bot.send_message(message.chat.id, "Нажмите на кнопку, для того чтобы узнать информацию об учете индивидуальных достижений", reply_markup=markup)
@bot.message_handler(commands=['video'])
def video_command(message):
    markup = types.InlineKeyboardMarkup()
    video_button = types.InlineKeyboardButton(text="Поступление | Как читать конкурсные списки", url="https://www.youtube.com/watch?v=XApUgBXJCD4&t=5s")
    markup.add(video_button)
    bot.send_message(message.chat.id, "Нажмите на кнопку, для того чтобы просмотреть видео с объяснением процедуры зачисления в ВУЗ", reply_markup=markup)

@bot.message_handler(commands=['programs'])
def programs_command(message):
    markup = types.InlineKeyboardMarkup()
    programs_button = types.InlineKeyboardButton(text="Программы обучения", url="https://rut-miit.ru/edu/programs")
    markup.add(programs_button)
    bot.send_message(message.chat.id, "Нажмите на кнопку, для того чтобы узнать информацию о программах обучения в ВУЗе", reply_markup=markup)

@bot.message_handler(commands=['special'])
def special_command(message):
    markup = types.InlineKeyboardMarkup()
    special_button = types.InlineKeyboardButton(text="Особые права при приёме", url="https://rut-miit.ru/admissions/office/136667")
    markup.add(special_button)
    bot.send_message(message.chat.id, "Нажмите на кнопку, для того чтобы узнать информацию о особых правах при приёме в ВУЗ", reply_markup=markup)

@bot.message_handler(commands=['min_points'])
def min_points_command(message):
    markup = types.InlineKeyboardMarkup()
    min_points_button = types.InlineKeyboardButton(text="Минимальные баллы", url="https://rut-miit.ru/admissions/office/128920")
    markup.add(min_points_button)
    bot.send_message(message.chat.id, "Нажмите на кнопку, для того чтобы узнать информацию о минимальных баллах, подтверждающее успешное прохождение вступительных испытаний", reply_markup=markup)

@bot.message_handler(commands=['contacts'])
def contacts_command(message):
    markup = types.InlineKeyboardMarkup()
    contacts_button = types.InlineKeyboardButton(text="Контактная информация", url="https://rut-miit.ru/contacts")
    markup.add(contacts_button)
    bot.send_message(message.chat.id, "Нажмите на кнопку, для того чтобы узнать контактную информацию", reply_markup=markup)

@bot.message_handler(commands=['cabinet'])
def cabinet_command(message):
    markup = types.InlineKeyboardMarkup()
    cabinet_button = types.InlineKeyboardButton(text="Личный кабинет", url="https://rut-miit.ru/cabinet/hello/login.jsp")
    markup.add(cabinet_button)
    bot.send_message(message.chat.id, "Нажмите на кнопку, для того чтобы перейти в личный кабинет абитуриента", reply_markup=markup)


bot.polling(none_stop=True, interval=0)  # постоянная проверка новых сообщений в боте
