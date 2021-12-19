import random
import telebot
import emoji
from telebot import types

bot = telebot.TeleBot("2108606220:AAFE2eafNBXl58BZFJ8ILeVRo2Ec4TGcPdY")  # создание бота


@bot.message_handler(commands=["start"])  # обработка команды /start
def start_command(message):
    bot.send_message(message.from_user.id, greetings, parse_mode="html")


@bot.message_handler(commands=["help"])  # обработка команды /help
def help_command(message):
    bot.send_message(message.from_user.id,
                     helptext + "\n\n" + helptext2 + "\n\n" + helptext3 + "\n\n" + helptext4 + "\n\n" +
                     helptext5 + "\n\n" + helptext6 + "\n\n" + helptext7 + "\n\n" + helptext8 + "\n\n" + helptext9 +
                     "\n\n" + helptext10 + "\n\n" + helptext11 + "\n\n" + helptext12 + "\n\n" + helptext13 + "\n\n" +
                     helptext14 + "\n\n" + helptext15, parse_mode="html")
    bot.send_message(message.from_user.id, "Для твоего удобства, все команды есть в меню, которое находится рядом с "
                                           "полем для ввода сообщения😌")


@bot.message_handler(commands=["reg"])  # обработка команды /reg
def registration(message):
    bot.send_message(message.from_user.id, "Ваше имя:")
    bot.register_next_step_handler(message, get_name)


@bot.message_handler(commands=["documents"])  # вывод URL-кнопки и информации о подаче документов + вывод картинки
def documents(message):
    markup = types.InlineKeyboardMarkup()
    docs_button = types.InlineKeyboardButton(text="Как подать документы", url="https://rut-miit.ru/admissions"
                                                                              "/office/48052")
    markup.add(docs_button)
    bot.send_photo(message.from_user.id, open("files/documents.png", "rb"), "Нажмите на кнопку, чтобы узнать как "
                                                                            "подать документы в РУТ(МИИТ)",
                   reply_markup=markup)


@bot.message_handler(commands=["account"])  # обработка команды /account
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


@bot.message_handler(commands=["sticker"])  # создание callback-кнопок
def sticker_sender(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("Веселые😀", callback_data="funny")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Грустные☹️", callback_data="sad")
    )
    bot.send_message(message.from_user.id, "Выбери категорию :)", reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)  # реакция на callback-кнопки (отправка стикеров)
def callback(query):
    data = query.data
    bot.edit_message_reply_markup(query.from_user.id, query.message.message_id)
    if data == "funny":
        bot.send_sticker(query.from_user.id, random.choice(funnystickers))
    elif data == "sad":
        bot.send_sticker(query.from_user.id, random.choice(sadstickers))


@bot.message_handler(commands=["achievements"])
def achievements_command(message):
    markup = types.InlineKeyboardMarkup()
    ach_button = types.InlineKeyboardButton(text="Продробнее об индивидуальных достижениях",
                                            url="https://www.miit.ru/admissions/office/136668")
    markup.add(ach_button)
    bot.send_message(message.chat.id,
                     "При приёме на обучение по программам бакалавриата, программам специалитета поступающему может "
                     "быть начислено за индивидуальные достижения *не более 10 баллов суммарно.*",
                     parse_mode="markdown",
                     reply_markup=markup)


@bot.message_handler(commands=["video"])
def video_command(message):
    bot.send_message(message.chat.id, "[Объяснение процедуры зачисления в ВУЗ.](youtube.com/watch?v=XApUgBXJCD4)",
                     parse_mode="markdown")


@bot.message_handler(commands=["programs"])
def programs_command(message):
    markup = types.InlineKeyboardMarkup()
    programs_button = types.InlineKeyboardButton(text="Программы обучения", url="https://rut-miit.ru/edu/programs")
    markup.add(programs_button)
    bot.send_message(message.chat.id,
                     "Нажмите на кнопку, для того чтобы узнать информацию о программах обучения в ВУЗе",
                     reply_markup=markup)


@bot.message_handler(commands=["special"])
def special_command(message):
    markup = types.InlineKeyboardMarkup()
    special_button = types.InlineKeyboardButton(text="Подробнее об особых правах при приёме",
                                                url="https://rut-miit.ru/admissions/office/136667")
    markup.add(special_button)
    bot.send_message(message.chat.id,
                     "*Право на прием без вступительных испытаний имеют:*" + "\n\n" + "*•* победители и призеры "
                                                                                      "заключительного этапа "
                                                                                      "всероссийской олимпиады "
                                                                                      "школьников" + "\n\n" +
                     "*•* победители и призеры IV этапа всеукраинских ученических олимпиад" + "\n\n" + "*•* чемпионы и "
                                                                                                       "призеры "
                                                                                                       "Олимпийских "
                                                                                                       "игр, "
                                                                                                       "Паралимпийских "
                                                                                                       "игр и "
                                                                                                       "Сурдлимпийских "
                                                                                                       "игр, "
                                                                                                       "чемпионы мира, "
                                                                                                       "чемпионы "
                                                                                                       "Европы",
                     parse_mode="markdown",
                     reply_markup=markup)


@bot.message_handler(commands=["min_points"])
def min_points_command(message):
    markup = types.InlineKeyboardMarkup()
    min_points_button = types.InlineKeyboardButton(text="Минимальные баллы для каждой специальности",
                                                   url="https://rut-miit.ru/admissions/office/128920")
    markup.add(min_points_button)
    bot.send_message(message.chat.id,
                     "*Примерное значение минимальных баллов по предметам ЕГЭ такое:*" + "\n\n" + "Русский язык: *40*;"
                     + "\n" + "Математика: *33*;" + "\n" + "Физика: *39*;" + "\n" + "Информатика и ИКТ: *44*;" + "\n" + "Обществознание: *45*;"
                     + "\n" + "Иностранный язык: *30*;" + "\n" + "История: *35*." + "\n\n" +
                     "***Эти баллы лишь приблизительные, на каждом направлении минимальные баллы свои***, нажмите на "
                     "кнопку ниже, чтобы ознакомиться с подробной информацией.", parse_mode="markdown",
                     reply_markup=markup)


@bot.message_handler(commands=["contacts"])
def contacts_command(message):
    markup = types.InlineKeyboardMarkup()
    contacts_button = types.InlineKeyboardButton(text="Полная контактная информация",
                                                 url="https://rut-miit.ru/contacts")
    markup.add(contacts_button)
    bot.send_message(message.chat.id, "*Приемная комиссия*" + "\n" + "Телефон: [+74952602332]("
                                                                     "tel:+74952602332)" + "\n" + "E-mail: "
                                                                                                  "pk@rut-miit.ru",
                     reply_markup=markup, parse_mode="markdown")


@bot.message_handler(commands=["cabinet"])
def cabinet_command(message):
    markup = types.InlineKeyboardMarkup()
    cabinet_button = types.InlineKeyboardButton(text="Регистрация личного кабинета",
                                                url="https://rut-miit.ru/reg/")
    markup.add(cabinet_button)
    bot.send_message(message.chat.id, "Для подачи документов вам необходимо *зарегистрировать личный кабинет*, "
                                      "нажмите на кнопку ниже, чтобы попасть прямо на страницу регистрации.",
                     parse_mode="markdown",
                     reply_markup=markup)


@bot.message_handler(commands=["faq"])  # обработка команды /faq
def faq(message):
    question1 = "<b>-Когда проводятся вступительные испытания для поступающих на бакалавр/специалитет?</b>"
    answer1 = "\n-Каждый вторник и четверг в 11:00 начиная с 29 июня."
    bot.send_message(message.from_user.id, question1 + answer1, parse_mode="html")
    question2 = "<b>-До какого срока проводятся вступительные испытания для поступающих на бакалавр/специалитет?</b>"
    answer2 = "\n-Для очной и очно-заочной формы: бюджетные места до 27 июля, а платные до 26 августа." \
              "\n-Для заочной формы до 31 августа."

    keyboard = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text="Дополнительная информация о приёмной комиссии",
                                         url="https://rut-miit.ru/admissions/office/about")
    keyboard.add(button1)

    bot.send_message(message.from_user.id, question2 + answer2, parse_mode="html", reply_markup=keyboard)


@bot.message_handler(commands=["hostel"])  # обработка команды /hostel
def hostel(message):
    text = "Российский университет транспорта (МИИТ) имеет в своём составе 10 комфортабельных общежитий." \
           "\nСтудент может получить место в общежитии при условии, что он иногородний или входит в льготные группы." \
           "\nСтоимость комнат в общежитии меньше стоимости снятия частных комнат, и зависит от заселённости и " \
           "качества помещения. "
    keyboard = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text="Дополнительная информация об общежитиях",
                                         url="https://rut-miit.ru/org/dormitory")
    keyboard.add(button1)
    bot.send_message(message.from_user.id, text=text, parse_mode="html", reply_markup=keyboard)


@bot.message_handler(commands=["news"])  # обработка команды /news
def news(message):
    keyboard = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text="Новости университета",
                                         url="https://rut-miit.ru/news?from=1&to=1&category_id=1383,1384,1703,1683,"
                                             "1743,1543,1158,1523,1803,1805,1147,1282,34,1148,1323,1563,1051,1643,"
                                             "1843,1583,1603,1127,1363")
    keyboard.add(button1)
    bot.send_message(message.from_user.id, text="<b>Ссылка на новости:</b>", parse_mode="html", reply_markup=keyboard)


@bot.message_handler(commands=["reviews"])  # обработка команды /reviews
def reviews(message):
    keyboard = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text="otzovik.com",
                                         url="https://otzovik.com/reviews"
                                             "/rossiyskiy_universitet_transporta_miit_russia_moscow/")
    button2 = types.InlineKeyboardButton(text="tabiturient.ru",
                                         url="https://tabiturient.ru/vuzu/miit/")
    button3 = types.InlineKeyboardButton(text="yandex.ru",
                                         url="https://yandex.ru/maps/org/rossiyskiy_universitet_transporta/1855876449"
                                             "/reviews/?ll=37.608007%2C55.787839&z=17")
    keyboard.add(button1, button2)
    keyboard.add(button3)
    bot.send_message(message.from_user.id, text="<b>Отзывы о РУТ(МИИТ) на сайте:</b>", parse_mode="html",
                     reply_markup=keyboard)


@bot.message_handler(func=lambda message: True, content_types=["sticker"])
def handle_sticker(message):
    bot.delete_message(message.from_user.id, message.message_id)
    bot.send_sticker(message.from_user.id, random.choice(funnystickers))
    bot.send_message(message.chat.id, "Я обменял твой стикер на свой!🙃" + "\n" + "Эй, если хочешь стикер на выбор, "
                                                                                  "используй /sticker. Только тсс..🤫")


@bot.message_handler(content_types=["document", "audio", "photo"])
def handle_docs_audio_photo(message):
    bot.send_message(message.from_user.id, "Мне это очень нравится!😍")


@bot.message_handler(content_types="text")  # реакция на сообщения вне функций
def get_text_messages(message):
    if message.text.lower() == "привет":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    elif message.text.lower() == "как подать документы?":
        documents(message)
    elif emoji.is_emoji(message.text):
        bot.delete_message(message.from_user.id, message.message_id)
        bot.send_message(message.from_user.id, random.choice(emoji1))
        bot.send_message(message.chat.id,
                         "Я обменял твой эмоджи на свой!🙃" + "\n" + "Эй, если хочешь стикер на выбор, "
                                                                     "используй /sticker. Только тсс..🤫")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю, пока только учу человеческий😞" + "\n" +
                         "Используй /help, чтобы узнать, что я умею.")


greetings = "Доброго времени суток, <b>я - Бот</b>, созданный для помощи абитуриентам, которые рассматривают РУТ(" \
            "МИИТ) для поступления. Используй /help, чтобы узнать, чем я могу тебе помочь."
helptext = "Хочешь получить рандомный стикер из выбранной катергории? Используй /sticker"
helptext2 = "Хочешь зарегистрироваться? Используй /reg"
helptext3 = "Уже зарегистрирован? Получи информацию о своем аккаунте командой /account"
helptext4 = "Хочешь узнать, как подать документы в РУТ(МИИТ)? Используй /documents"
helptext5 = "Хочешь узнать об условиях предоставления общежития? Используй /hostel"
helptext6 = "Чтобы узнать ответы на часто задаваемые вопросы используй /faq"
helptext7 = "Хочешь узнать отзывы об университете? Используй /reviews"
helptext8 = "Чтобы узнать о новостях университета используй /news"
helptext9 = "Хочешь узнать информацию об учете индивидуальных достижений? Используй /achievements"
helptext10 = "Хочешь узнать, как проходит процедура зачисления в ВУЗ? Используй /video"
helptext11 = "Хочешь узнать информацию о программах обучения в ВУЗе? Используй /programs"
helptext12 = "Хочешь узнать информацию о особых правах при приёме в ВУЗ? Используй /special"
helptext13 = "Хочешь о минимальных баллах, подтверждающее успешное прохождение вступительных испытаний? Используй " \
             "/min_points "
helptext14 = "Хочешь узнать контактную информацию? Используй /contacts"
helptext15 = "Хочешь перейти в личный кабинет абитуриента? Используй /cabinet"
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
               "CAACAgIAAxkBAAEDelBht5Qz0fyCwkyOlIL9LXc0t96CGwACxAEAAhZCawqGm0hPypIWwiME",
               "CAACAgQAAxkBAAEDP3RhitEJoRWmgUZWMBDLRfB6A1ED6AACYhEAAswdmwytUMTpt2oDkSIE"
               ]
emoji1 = ["😎", "😌", "🙂", "😇", "😛", "😚", "😉"]


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
                         parse_mode="markdown")
    elif message.text.lower() == "нет":
        bot.send_message(message.from_user.id, "Используйте /reg, чтобы повторно пройти регистрацию.",
                         reply_markup=types.ReplyKeyboardRemove(), parse_mode="markdown")


bot.polling(none_stop=True, interval=0)  # постоянная проверка новых сообщений в боте
