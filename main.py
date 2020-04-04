import covid
import COVID19Py
import telebot
from telebot import types
from covid import Covid

covid = Covid()
covid19 = COVID19Py.COVID19()
bot = telebot.TeleBot('')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton("Мир 🌎")
    btn2 = types.KeyboardButton("Россия 🇷🇺")
    btn3 = types.KeyboardButton("Сша 🇺🇸")
    btn4 = types.KeyboardButton("Китай 🇨🇳")
    btn5 = types.KeyboardButton("Испания 🇪🇸")
    btn6 = types.KeyboardButton("Италия 🇮🇹")
    btn7 = types.KeyboardButton("Германия 🇩🇪")
    btn8 = types.KeyboardButton("Франция 🇫🇷")
    btn9 = types.KeyboardButton("Иран 🇮🇷")
    btn10 = types.KeyboardButton("Великобритания 🇬🇧")
    btn11 = types.KeyboardButton("Турция 🇹🇷")
    btn12 = types.KeyboardButton("Бельгия 🇧🇪")
    btn13 = types.KeyboardButton("Нидерланды 🇳🇱")
    btn14 = types.KeyboardButton("Австрия 🇦🇹")
    btn15 = types.KeyboardButton("Южная Корея 🇰🇷")
    btn16 = types.KeyboardButton("Канада 🇨🇦")
    btn17 = types.KeyboardButton("Португалия 🇵🇹")
    btn18 = types.KeyboardButton("Бразилия 🇧🇷")
    btn19 = types.KeyboardButton("Израиль 🇮🇱")
    btn20 = types.KeyboardButton("Швеция 🇸🇪")
    btn21 = types.KeyboardButton("Австралия 🇦🇺")
    btn22 = types.KeyboardButton("Норвегия 🇳🇴")
    btn23 = types.KeyboardButton("Кыргызстан 🇰🇬")
    btn24 = types.KeyboardButton("Полезная информация 📖")
    btn25 = types.KeyboardButton("Обновить бота 🔨")
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8,
               btn9, btn10, btn11, btn12, btn13, btn14, btn15, btn16, btn17, btn18, btn19, btn20, btn21, btn22, btn23, btn24, btn25)

    send_mess = f"<b>Приветствую {message.from_user.first_name}!</b>\nВведи страну и узнай о статистике на данный момент"
    bot.send_message(message.chat.id, send_mess,
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def mess(message):
    final_message = ""
    get_message_bot = message.text.strip().upper()
    if get_message_bot == "США 🇺🇸":
        location = covid.get_status_by_country_id(18)
        somelocation = covid19.getLocationByCountryCode("US")
    elif get_message_bot == "РОССИЯ 🇷🇺":
        location = covid.get_status_by_country_id(14)
        somelocation = covid19.getLocationByCountryCode("RU")
    elif get_message_bot == "КИТАЙ 🇨🇳":
        location = covid.get_status_by_country_id(4)
        somelocation = covid19.getLocationByCountryCode("CN")
    elif get_message_bot == "ИСПАНИЯ 🇪🇸":
        location = covid.get_status_by_country_id(159)
        somelocation = covid19.getLocationByCountryCode("ES")
    elif get_message_bot == "ИТАЛИЯ 🇮🇹":
        location = covid.get_status_by_country_id(11)
        somelocation = covid19.getLocationByCountryCode("IT")
    elif get_message_bot == "ГЕРМАНИЯ 🇩🇪":
        location = covid.get_status_by_country_id(8)
        somelocation = covid19.getLocationByCountryCode("DE")
    elif get_message_bot == "ФРАНЦИЯ 🇫🇷":
        location = covid.get_status_by_country_id(7)
        somelocation = covid19.getLocationByCountryCode("FR")
    elif get_message_bot == "ИРАН 🇮🇷":
        location = covid.get_status_by_country_id(90)
        somelocation = covid19.getLocationByCountryCode("IR")
    elif get_message_bot == "ВЕЛИКОБРИТАНИЯ 🇬🇧":
        location = covid.get_status_by_country_id(17)
        somelocation = covid19.getLocationByCountryCode("GB")
    elif get_message_bot == "ТУРЦИЯ 🇹🇷":
        location = covid.get_status_by_country_id(171)
        somelocation = covid19.getLocationByCountryCode("TR")
    elif get_message_bot == "БЕЛЬГИЯ 🇧🇪":
        location = covid.get_status_by_country_id(33)
        somelocation = covid19.getLocationByCountryCode("BE")
    elif get_message_bot == "НИДЕРЛАНДЫ 🇳🇱":
        location = covid.get_status_by_country_id(12)
        somelocation = covid19.getLocationByCountryCode("NL")
    elif get_message_bot == "АВСТРИЯ 🇦🇹":
        location = covid.get_status_by_country_id(2)
        somelocation = covid19.getLocationByCountryCode("AT")
    elif get_message_bot == "ЮЖНАЯ КОРЕЯ 🇰🇷":
        location = covid.get_status_by_country_id(98)
        somelocation = covid19.getLocationByCountryCode("KR")
    elif get_message_bot == "КАНАДА 🇨🇦":
        location = covid.get_status_by_country_id(3)
        somelocation = covid19.getLocationByCountryCode("CA")
    elif get_message_bot == "ПОРТУГАЛИЯ 🇵🇹":
        location = covid.get_status_by_country_id(141)
        somelocation = covid19.getLocationByCountryCode("PT")
    elif get_message_bot == "БРАЗИЛИЯ 🇧🇷":
        location = covid.get_status_by_country_id(40)
        somelocation = covid19.getLocationByCountryCode("BR")
    elif get_message_bot == "ИЗРАИЛЬ 🇮🇱":
        location = covid.get_status_by_country_id(92)
        somelocation = covid19.getLocationByCountryCode("IL")
    elif get_message_bot == "ШВЕЦИЯ 🇸🇪":
        location = covid.get_status_by_country_id(15)
        somelocation = covid19.getLocationByCountryCode("SE")
    elif get_message_bot == "АВСТРАЛИЯ 🇦🇺":
        location = covid.get_status_by_country_id(1)
        somelocation = covid19.getLocationByCountryCode("AU")
    elif get_message_bot == "НОРВЕГИЯ 🇳🇴":
        location = covid.get_status_by_country_id(13)
        somelocation = covid19.getLocationByCountryCode("NO")
    elif get_message_bot == "КЫРГЫЗСТАН 🇰🇬":
        location = covid.get_status_by_country_id(101)
        somelocation = covid19.getLocationByCountryCode("KG")
    elif get_message_bot == "ПОЛЕЗНАЯ ИНФОРМАЦИЯ 📖":
        final_message = f"<u>Ниже предоставлены полезные сервисы</u>\n"'<a href="https://cutt.ly/ZtOyAAB"><b>Онйлайн карта/статистика</b> (ENG)</a>.\n''<a href="https://cutt.ly/wtOynXs"><b>Онйлайн карта/статистика</b> (RU)</a>.\n''<a href="https://cutt.ly/ctOy2BZ"><b>Информация о новой коронавирусной инфекции</b> (RU)</a>.\n''<a href="https://cutt.ly/2tOurco"><b>Профилактика коронавируса</b> (RU)</a>.\n''<a href="https://cutt.ly/OtOuE55"><b>Информация ВОЗ</b> (RU)(ENG)</a>.\n''<a href="https://cutt.ly/ItOuTYi"><b>Симптомы ВОЗ</b> (RU)(ENG)</a>.\n''<a href="https://cutt.ly/7tOuUDr"><b>Коронавирус вопросы и ответы ВОЗ</b> (RU)(ENG)</a>.\n'
    elif get_message_bot == "ОБНОВИТЬ БОТА 🔨":
        final_message = f"Команда для обновления бота /start"

    else:
        confirmed_world = covid.get_total_confirmed_cases()
        recovered_world = covid.get_total_recovered()
        deaths_world = covid.get_total_deaths()
        final_message = f"<u>Данные по всему миру:</u>\n"f"<b>Зараженные: </b>{confirmed_world:,}\n"f"<b>Выздоровели: </b>{recovered_world:,}\n"f"<b>Смертей: </b>{deaths_world:,}\n"

    if final_message == "":
        date = somelocation[0]['last_updated'].split("T")
        time = date[1].split(".")
        final_message = f"<u>Последнее обновление:</u>\n{date[0]} | {time[0]}\n"f"<u>Последние данные:</u>\n"f"<b>Население: </b>{somelocation[0]['country_population']:,}\n"f"<b>Зараженные: </b>{location['confirmed']:,}\n"f"<b>Выздоровели: </b>{location['recovered']:,}\n"f"<b>Умерло: </b>{location['deaths']:,}\n"

    bot.send_message(message.chat.id, final_message, parse_mode='html')


bot.polling(none_stop=True)
