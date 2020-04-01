import COVID19Py
import telebot
from telebot import types

covid19 = COVID19Py.COVID19()
bot = telebot.TeleBot('')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton("Мир 🌎")
    btn2 = types.KeyboardButton("Россия 🇷🇺")
    btn3 = types.KeyboardButton("Украина 🇺🇦")
    btn4 = types.KeyboardButton("Сша 🇺🇸")
    btn5 = types.KeyboardButton("Китай 🇨🇳")
    btn6 = types.KeyboardButton("Испания 🇪🇸")
    btn7 = types.KeyboardButton("Италия 🇮🇹")
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)




    send_mess = f"<b>Приветствую {message.from_user.first_name}!</b>\nВведи страну и узнай о статистике на данный момент"
    bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def mess(message):
    final_message = ""
    get_message_bot = message.text.strip().upper()
    if get_message_bot == "США 🇺🇸":
        location = covid19.getLocationByCountryCode("US")
    elif get_message_bot == "УКРАИНА 🇺🇦":
        location = covid19.getLocationByCountryCode("UA")
    elif get_message_bot == "РОССИЯ 🇷🇺":
        location = covid19.getLocationByCountryCode("RU")
    elif get_message_bot == "КИТАЙ 🇨🇳":
        location = covid19.getLocationByCountryCode("CN")
    elif get_message_bot == "ИСПАНИЯ 🇪🇸":
        location = covid19.getLocationByCountryCode("ES")
    elif get_message_bot == "ИТАЛИЯ 🇮🇹":
        location = covid19.getLocationByCountryCode("IT")
    else:
        location = covid19.getAll()
        final_message = f"<u>Данные по всему миру:</u>\n<b>Зараженные: </b>{location['confirmed']:,}\n<b>Смертей: </b>{location['deaths']:,}\n"

    if final_message == "":
        date = location[0]['last_updated'].split("T")
        time = date[1].split(".")
        final_message = f"<u>Данные по стране:</u>\nНаселение: {location[0]['country_population']:,}\n"f"<u>Последнее обновление:</u>\n{date[0]} | {time[0]}\n<b>Последние данные:</b>\n"f"<b>Зараженных: </b>{location[0]['confirmed']:,}\n<b>Смертей: </b>"f"{location[0]['deaths']:,}\n"

    bot.send_message(message.chat.id, final_message, parse_mode='html')

bot.polling(none_stop=True)
