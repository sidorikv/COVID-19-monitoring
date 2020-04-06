import covid
import COVID19Py
import telebot
from telebot import types
from covid import Covid

covid = Covid()
covid19 = COVID19Py.COVID19()
bot = telebot.TeleBot('')


@bot.message_handler(commands=['start', 'update'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton("Миp 🌎")
    btn2 = types.KeyboardButton("Рoссия 🇷🇺")
    btn3 = types.KeyboardButton("Укрaина 🇺🇦")
    btn4 = types.KeyboardButton("Сшa 🇺🇸")
    btn5 = types.KeyboardButton("Китaй 🇨🇳")
    btn6 = types.KeyboardButton("Испaния 🇪🇸")
    btn7 = types.KeyboardButton("Итaлия 🇮🇹")
    btn8 = types.KeyboardButton("Гермaния 🇩🇪")
    btn9 = types.KeyboardButton("Фрaнция 🇫🇷")
    btn10 = types.KeyboardButton("Ирaн 🇮🇷")
    btn11 = types.KeyboardButton("Великобритaния 🇬🇧")
    btn12 = types.KeyboardButton("Tурция 🇹🇷")
    btn13 = types.KeyboardButton("Бeльгия 🇧🇪")
    btn14 = types.KeyboardButton("Нидeрланды 🇳🇱")
    btn15 = types.KeyboardButton("Aвстрия 🇦🇹")
    btn16 = types.KeyboardButton("Южнaя Корея 🇰🇷")
    btn17 = types.KeyboardButton("Канадa 🇨🇦")
    btn18 = types.KeyboardButton("Пoртугалия 🇵🇹")
    btn19 = types.KeyboardButton("Брaзилия 🇧🇷")
    btn20 = types.KeyboardButton("Изрaиль 🇮🇱")
    btn21 = types.KeyboardButton("Швeция 🇸🇪")
    btn22 = types.KeyboardButton("Aвстралия 🇦🇺")
    btn23 = types.KeyboardButton("Нoрвегия 🇳🇴")
    btn24 = types.KeyboardButton("Кыpгызстан 🇰🇬")
    btn25 = types.KeyboardButton("Пoльша 🇵🇱")
    btn26 = types.KeyboardButton("Pумыния 🇷🇴")
    btn27 = types.KeyboardButton("Эквaдор 🇪🇨")
    btn28 = types.KeyboardButton("Пaкистан 🇵🇰")
    btn29 = types.KeyboardButton("Пeру 🇵🇪")
    btn30 = types.KeyboardButton("Мoлдавия 🇲🇩")
    btn31 = types.KeyboardButton("Полезная информация 📖")
    btn32 = types.KeyboardButton("Обновить бота 🔨")
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8,
               btn9, btn10, btn11, btn12, btn13, btn14, btn15, btn16, btn17, btn18, btn19, btn20, btn21, btn22, btn23, btn24, btn25, btn26, btn27, btn28, btn29, btn30, btn31, btn32)

    send_mess = f"<b>Приветствую {message.from_user.first_name}!</b>\nВведи страну и узнай о статистике на данный момент"
    bot.send_message(message.chat.id, send_mess,
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def mess(message):
    final_message = ""
    get_message_bot = message.text.strip().upper()
    if get_message_bot == "МИP 🌎":
        confirmed_world = covid.get_total_confirmed_cases()
        recovered_world = covid.get_total_recovered()
        deaths_world = covid.get_total_deaths()
        final_message = f"<u>Данные по всему миру:</u>\n"f"<b>Зараженные: </b>{confirmed_world:,}\n"f"<b>Выздоровели: </b>{recovered_world:,}\n"f"<b>Смертей: </b>{deaths_world:,}\n"
    elif get_message_bot == "СШA 🇺🇸":
        location = covid.get_status_by_country_id(18)
        somelocation = covid19.getLocationByCountryCode("US")
    elif get_message_bot == "РOССИЯ 🇷🇺":
        location = covid.get_status_by_country_id(14)
        somelocation = covid19.getLocationByCountryCode("RU")
    elif get_message_bot == "УКРAИНА 🇺🇦":
        location = covid.get_status_by_country_id(174)
        somelocation = covid19.getLocationByCountryCode("UA")
    elif get_message_bot == "КИТAЙ 🇨🇳":
        location = covid.get_status_by_country_id(4)
        somelocation = covid19.getLocationByCountryCode("CN")
    elif get_message_bot == "ИСПAНИЯ 🇪🇸":
        location = covid.get_status_by_country_id(160)
        somelocation = covid19.getLocationByCountryCode("ES")
    elif get_message_bot == "ИТAЛИЯ 🇮🇹":
        location = covid.get_status_by_country_id(11)
        somelocation = covid19.getLocationByCountryCode("IT")
    elif get_message_bot == "ГЕРМAНИЯ 🇩🇪":
        location = covid.get_status_by_country_id(8)
        somelocation = covid19.getLocationByCountryCode("DE")
    elif get_message_bot == "ФРAНЦИЯ 🇫🇷":
        location = covid.get_status_by_country_id(7)
        somelocation = covid19.getLocationByCountryCode("FR")
    elif get_message_bot == "ИРAН 🇮🇷":
        location = covid.get_status_by_country_id(90)
        somelocation = covid19.getLocationByCountryCode("IR")
    elif get_message_bot == "ВЕЛИКОБРИТAНИЯ 🇬🇧":
        location = covid.get_status_by_country_id(17)
        somelocation = covid19.getLocationByCountryCode("GB")
    elif get_message_bot == "TУРЦИЯ 🇹🇷":
        location = covid.get_status_by_country_id(172)
        somelocation = covid19.getLocationByCountryCode("TR")
    elif get_message_bot == "БEЛЬГИЯ 🇧🇪":
        location = covid.get_status_by_country_id(33)
        somelocation = covid19.getLocationByCountryCode("BE")
    elif get_message_bot == "НИДEРЛАНДЫ 🇳🇱":
        location = covid.get_status_by_country_id(12)
        somelocation = covid19.getLocationByCountryCode("NL")
    elif get_message_bot == "AВСТРИЯ 🇦🇹":
        location = covid.get_status_by_country_id(2)
        somelocation = covid19.getLocationByCountryCode("AT")
    elif get_message_bot == "ЮЖНAЯ КОРЕЯ 🇰🇷":
        location = covid.get_status_by_country_id(98)
        somelocation = covid19.getLocationByCountryCode("KR")
    elif get_message_bot == "КАНАДA 🇨🇦":
        location = covid.get_status_by_country_id(3)
        somelocation = covid19.getLocationByCountryCode("CA")
    elif get_message_bot == "ПOРТУГАЛИЯ 🇵🇹":
        location = covid.get_status_by_country_id(141)
        somelocation = covid19.getLocationByCountryCode("PT")
    elif get_message_bot == "БРAЗИЛИЯ 🇧🇷":
        location = covid.get_status_by_country_id(40)
        somelocation = covid19.getLocationByCountryCode("BR")
    elif get_message_bot == "ИЗРAИЛЬ 🇮🇱":
        location = covid.get_status_by_country_id(92)
        somelocation = covid19.getLocationByCountryCode("IL")
    elif get_message_bot == "ШВEЦИЯ 🇸🇪":
        location = covid.get_status_by_country_id(15)
        somelocation = covid19.getLocationByCountryCode("SE")
    elif get_message_bot == "AВСТРАЛИЯ 🇦🇺":
        location = covid.get_status_by_country_id(1)
        somelocation = covid19.getLocationByCountryCode("AU")
    elif get_message_bot == "НOРВЕГИЯ 🇳🇴":
        location = covid.get_status_by_country_id(13)
        somelocation = covid19.getLocationByCountryCode("NO")
    elif get_message_bot == "КЫPГЫЗСТАН 🇰🇬":
        location = covid.get_status_by_country_id(101)
        somelocation = covid19.getLocationByCountryCode("KG")
    elif get_message_bot == "ПOЛЬША 🇵🇱":
        location = covid.get_status_by_country_id(140)
        somelocation = covid19.getLocationByCountryCode("PL")
    elif get_message_bot == "PУМЫНИЯ 🇷🇴":
        location = covid.get_status_by_country_id(143)
        somelocation = covid19.getLocationByCountryCode("RO")
    elif get_message_bot == "ЭКВAДОР 🇪🇨":
        location = covid.get_status_by_country_id(65)
        somelocation = covid19.getLocationByCountryCode("EC")
    elif get_message_bot == "ПAКИСТАН 🇵🇰":
        location = covid.get_status_by_country_id(134)
        somelocation = covid19.getLocationByCountryCode("PK")
    elif get_message_bot == "ПEРУ 🇵🇪":
        location = covid.get_status_by_country_id(138)
        somelocation = covid19.getLocationByCountryCode("PE")
    elif get_message_bot == "МOЛДАВИЯ 🇲🇩":
        location = covid.get_status_by_country_id(120)
        somelocation = covid19.getLocationByCountryCode("MD")
    elif get_message_bot == "ПОЛЕЗНАЯ ИНФОРМАЦИЯ 📖":
        final_message = f"<u>Ниже предоставлены полезные сервисы</u>\n"'<a href="https://cutt.ly/ZtOyAAB"><b>Онйлайн карта/статистика</b> (ENG)</a>.\n''<a href="https://cutt.ly/wtOynXs"><b>Онйлайн карта/статистика</b> (RU)</a>.\n''<a href="https://cutt.ly/ctOy2BZ"><b>Информация о новой коронавирусной инфекции</b> (RU)</a>.\n''<a href="https://cutt.ly/2tOurco"><b>Профилактика коронавируса</b> (RU)</a>.\n''<a href="https://cutt.ly/OtOuE55"><b>Информация ВОЗ</b> (RU)(ENG)</a>.\n''<a href="https://cutt.ly/ItOuTYi"><b>Симптомы ВОЗ</b> (RU)(ENG)</a>.\n''<a href="https://cutt.ly/7tOuUDr"><b>Коронавирус вопросы и ответы ВОЗ</b> (RU)(ENG)</a>.\n'
    elif get_message_bot == "ОБНОВИТЬ БОТА 🔨":
        return start(message)

    else:
        final_message = f"<b>Либо вы ошиблись фразой, либо версия вашего бота устарела. Для обновления бота воспользуйтесь кнопкой в самом низу!</b>"

    if final_message == "":
        date = somelocation[0]['last_updated'].split("T")
        time = date[1].split(".")
        final_message = f"<u>Последнее обновление:</u>\n{date[0]} | {time[0]}\n"f"<u>Последние данные:</u>\n"f"<b>Население: </b>{somelocation[0]['country_population']:,}\n"f"<b>Зараженные: </b>{location['confirmed']:,}\n"f"<b>Выздоровели: </b>{location['recovered']:,}\n"f"<b>Умерло: </b>{location['deaths']:,}\n"

    bot.send_message(message.chat.id, final_message, parse_mode='html')


bot.polling(none_stop=True)
