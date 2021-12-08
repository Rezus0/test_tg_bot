import telebot
from telebot import types

bot = telebot.TeleBot("")

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

bot.polling(none_stop=True)
