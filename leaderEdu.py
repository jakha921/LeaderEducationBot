import telebot
from telebot import types
from config import TOKEN

bot = telebot.TeleBot(
    TOKEN, parse_mode="html")

lang = ''


@bot.message_handler(commands=['start', 'news'])
def get_lang(message):
    if (message.text == '/start'):
        markup = types.ReplyKeyboardMarkup()
        ru = types.KeyboardButton("🇷🇺Руский")
        uz = types.KeyboardButton("🇺🇿O`zbek")
        us = types.KeyboardButton("🇺🇸English")
        markup.row(ru, uz, us)
        bot.send_message(message.chat.id, "<em>Выберите язык интерфейса💬</em>")
        bot.send_message(message.chat.id, '<em>Tilini tanlang💬</em>')
        bot.send_message(
            message.chat.id, '<em>Choose language💬</em>', reply_markup=markup)
    else:
        pass


# menu

def get_menu(message, lang):
    markup = types.ReplyKeyboardMarkup()
    if(lang == 'ru'):
        ourCourses = types.KeyboardButton("Наши курсы")
        onlineTest = types.KeyboardButton("Онлайн тест")
        contacts = types.KeyboardButton("Контакты")
        langg = types.KeyboardButton("Смена языка")
        callback = types.KeyboardButton("Обратный звонок")
        about = types.KeyboardButton("О нас")
        markup.row(ourCourses)
        markup.row(onlineTest, contacts)
        markup.row(callback, about)
        markup.row(langg)
        bot.send_message(message.chat.id, "Главное меню", reply_markup=markup)

    if(lang == 'uz'):
        ourCourses = types.KeyboardButton("Kurslarimiz")
        onlineTest = types.KeyboardButton("Onlayn test")
        contacts = types.KeyboardButton("Contactlarimiz")
        langg = types.KeyboardButton("Tilini o'zgartirish")
        callback = types.KeyboardButton("Qung`roq qilish")
        about = types.KeyboardButton("Biza haqimizda")
        markup.row(ourCourses)
        markup.row(onlineTest, contacts)
        markup.row(callback, about)
        markup.row(langg)
        bot.send_message(message.chat.id, "Bosh menu", reply_markup=markup)

    if(lang == 'us'):
        ourCourses = types.KeyboardButton("Our courses")
        onlineTest = types.KeyboardButton("Online test")
        contacts = types.KeyboardButton("Contacts")
        langg = types.KeyboardButton("Change the language")
        callback = types.KeyboardButton("Callback")
        about = types.KeyboardButton("About us")
        markup.row(ourCourses)
        markup.row(onlineTest, contacts)
        markup.row(callback, about)
        markup.row(langg)
        bot.send_message(message.chat.id, "Main menu", reply_markup=markup)


# ourCourses

def get_ourCourses(call, lang):
    markup = types.ReplyKeyboardMarkup()
    if(lang == 'ru'):
        fastCourse = types.KeyboardButton("Бытрые курсы")
        intensiveCourse = types.KeyboardButton("Интинсивные курсы")
        easyCourse = types.KeyboardButton("Лекие курсы")
        Course = types.KeyboardButton("Обычные курсы")
        get_menu = types.KeyboardButton("🔙Главное меню")
        markup.row(fastCourse, intensiveCourse)
        markup.row(easyCourse, Course)
        markup.row(get_menu)
        bot.send_message(call.chat.id, "Выберите курс", reply_markup=markup)

    if(lang == 'uz'):
        fastCourse = types.KeyboardButton("Tezkor kurslar")
        intensiveCourse = types.KeyboardButton("Intensiv kurslar")
        easyCourse = types.KeyboardButton("Osan kurslar")
        Course = types.KeyboardButton("Oddiy kurslar")
        get_menu = types.KeyboardButton("🔙Bosh menu")
        markup.row(fastCourse, intensiveCourse)
        markup.row(easyCourse, Course)
        markup.row(get_menu)
        bot.send_message(call.chat.id, "Kursni tanglang", reply_markup=markup)

    if(lang == 'us'):
        fastCourse = types.KeyboardButton("Fast courses")
        intensiveCourse = types.KeyboardButton("Intinsive courses")
        easyCourse = types.KeyboardButton("Easy courses")
        Course = types.KeyboardButton("Simple courses")
        get_menu = types.KeyboardButton("🔙Main menu")
        markup.row(fastCourse, intensiveCourse)
        markup.row(easyCourse, Course)
        markup.row(get_menu)
        bot.send_message(call.chat.id, "Choose your course",
                         reply_markup=markup)


# Corses


# fastInfo
def fastInfo(message, lang):
    markup = types.InlineKeyboardMarkup()
    if (lang == 'ru'):
        register = types.InlineKeyboardButton(
            "Регистрация", callback_data='reg')
        markup.add(register)
        bot.send_message(
            message.chat.id, "Fast course\n В неделю: 3 раза\nСколько времени в день: 1,5 часа\n\nСтоимоть занятие в месяц: 2 млн сумм\nLorem ipsum dolor sit amet consectetur adipisicing elit. \nAsperiores laboriosam dolores necessitatibus, \nblanditiis autem esse eos in impedit eveniet voluptatum \nincidunt ab quod, eaque minima error ducimus \nmollitia nihil quaerat. ", reply_markup=markup)

    if (lang == 'uz'):
        register = types.InlineKeyboardButton(
            "Regitrasiya qilish", callback_data='reg')
        markup.add(register)
        bot.send_message(
            message.chat.id, "Fast course\n В неделю: 3 раза\nСколько времени в день: 1,5 часа\n\nСтоимоть занятие в месяц: 2 млн сумм\nLorem ipsum dolor sit amet consectetur adipisicing elit. \nAsperiores laboriosam dolores necessitatibus, \nblanditiis autem esse eos in impedit eveniet voluptatum \nincidunt ab quod, eaque minima error ducimus \nmollitia nihil quaerat. ", reply_markup=markup)

    if (lang == 'us'):
        register = types.InlineKeyboardButton(
            "Registration", callback_data='reg')
        markup.add(register)
        bot.send_message(
            message.chat.id, "Fast course\n В неделю: 3 раза\nСколько времени в день: 1,5 часа\n\nСтоимоть занятие в месяц: 2 млн сумм\nLorem ipsum dolor sit amet consectetur adipisicing elit. \nAsperiores laboriosam dolores necessitatibus, \nblanditiis autem esse eos in impedit eveniet voluptatum \nincidunt ab quod, eaque minima error ducimus \nmollitia nihil quaerat. ", reply_markup=markup)


# FastInfo get_reg

def get_reg(message, lang):
    markup = types.KeyboardButton(
        request_contact=True, text="Отправить свои данный")
    if (lang == 'ru'):
        bot.send_message(types.MessageID, "Отправить свои данный",
                         reply_to_message_id="Мы скоро с вами свяжемся", reply_markup=markup)


# intensiveInfo
def intensiveInfo(message, lang):
    markup = types.InlineKeyboardMarkup()
    if (lang == 'ru'):
        register = types.InlineKeyboardButton(
            "Регистрация", callback_data='reg')
        testing = types.InlineKeyboardButton(
            "Получить тест", callback_data='test')
        markup.add(register, testing)
        bot.send_message(
            message.chat.id, "intensive course\n В неделю: 3 раза\nСколько времени в день: 1,5 часа\n\nСтоимоть занятие в месяц: 2 млн сумм\nLorem ipsum dolor sit amet consectetur adipisicing elit. \nAsperiores laboriosam dolores necessitatibus, \nblanditiis autem esse eos in impedit eveniet voluptatum \nincidunt ab quod, eaque minima error ducimus \nmollitia nihil quaerat. ", reply_markup=markup)

# intensiveInfo get_reg


# easyInfo
def easyInfo(message, lang):
    markup = types.InlineKeyboardMarkup()
    if (lang == 'ru'):
        register = types.InlineKeyboardButton(
            "Регистрация", callback_data='reg')
        markup.add(register)
        bot.send_message(
            message.chat.id, "easy course\n В неделю: 3 раза\nСколько времени в день: 1,5 часа\n\nСтоимоть занятие в месяц: 2 млн сумм\nLorem ipsum dolor sit amet consectetur adipisicing elit. \nAsperiores laboriosam dolores necessitatibus, \nblanditiis autem esse eos in impedit eveniet voluptatum \nincidunt ab quod, eaque minima error ducimus \nmollitia nihil quaerat. ", reply_markup=markup)


# CourseInfo
def CourseInfo(message, lang):
    markup = types.InlineKeyboardMarkup()
    if (lang == 'ru'):
        register = types.InlineKeyboardButton(
            "Регистрация", callback_data='reg')
        testing = types.InlineKeyboardButton(
            "Получить тест", callback_data='test')
        markup.add(register, testing)
        bot.send_message(
            message.chat.id, "simple course\n В неделю: 3 раза\nСколько времени в день: 1,5 часа\n\nСтоимоть занятие в месяц: 2 млн сумм\nLorem ipsum dolor sit amet consectetur adipisicing elit. \nAsperiores laboriosam dolores necessitatibus, \nblanditiis autem esse eos in impedit eveniet voluptatum \nincidunt ab quod, eaque minima error ducimus \nmollitia nihil quaerat. ", reply_markup=markup)


# onlineTest

def get_test(message):
    # photo = open('img/logo.png', 'rb')
    # bot.send_photo(message.from_user.id, photo)

    doc = open('tmp/file.txt', 'rb')
    bot.send_document(message.from_user.id, doc)

# Contacts


def get_contacts(message, lang):
    markup = types.InlineKeyboardMarkup()
    if (lang == 'ru'):
        location = types.InlineKeyboardButton(
            "📍 Геоданные", callback_data='location')
        markup.add(location)
        bot.send_message(message.chat.id, "Наше контакты:\nМеждународный бизнес центр \n(Tashkent Plaza, 1 этаж, \nориентир: 'НБУ')\n\nСоц. сеть\nFacebook: jakha921.com\nTelegramm: https://t.me.jakha921", reply_markup=markup)

    if (lang == 'uz'):
        location = types.InlineKeyboardButton(
            "📍 Geoloktsiya", callback_data='location')
        markup.add(location)
        bot.send_message(message.chat.id, "Наше контакты:\nМеждународный бизнес центр \n(Tashkent Plaza, 1 этаж, \nориентир: 'НБУ')\n\nСоц. сеть\nFacebook: jakha921.com\nTelegramm: https://t.me.jakha921", reply_markup=markup)

    if (lang == 'us'):
        location = types.InlineKeyboardButton(
            "📍 Locatioin", callback_data='location')
        markup.add(location)
        bot.send_message(message.chat.id, "Наше контакты:\nМеждународный бизнес центр \n(Tashkent Plaza, 1 этаж, \nориентир: 'НБУ')\n\nСоц. сеть\nFacebook: jakha921.com\nTelegramm: https://t.me.jakha921", reply_markup=markup)


# get_contact

def get_location(message):
    bot.send_location(message.from_user.id, latitude=41.3252, longitude=69.2323)


# get_callback

def get_callback(message):
    bot.send_contact(
        message.chat.id, phone_number="+998913339636", first_name="Jakha")


# about

def get_about(message, lang):
    if(lang == 'ru'):
        bot.send_message(message.chat.id, "О нас")
        photo = open('img/logo.png', 'rb')
        bot.send_photo(message.from_user.id, photo)
        bot.send_message(
            message.chat.id, "Lorem ipsum dolor sit amet consectetur adipisicing elit. Velit, inventore nihil deleniti harum eligendi sed deserunt\n\nLorem ipsum dolor sit amet consectetur adipisicing elit. Velit, inventore nihil deleniti harum eligendi sed deserunt")

    if(lang == 'uz'):
        bot.send_message(message.chat.id, "Biz haqimizda")
        photo = open('img/logo.png', 'rb')
        bot.send_photo(message.from_user.id, photo)
        bot.send_message(
            message.chat.id, "Lorem ipsum dolor sit amet consectetur adipisicing elit. Velit, inventore nihil deleniti harum eligendi sed deserunt\n\nLorem ipsum dolor sit amet consectetur adipisicing elit. Velit, inventore nihil deleniti harum eligendi sed deserunt")

    if(lang == 'us'):
        bot.send_message(message.chat.id, "About us")
        photo = open('img/logo.png', 'rb')
        bot.send_photo(message.from_user.id, photo)
        bot.send_message(
            message.chat.id, "Lorem ipsum dolor sit amet consectetur adipisicing elit. Velit, inventore nihil deleniti harum eligendi sed deserunt\n\nLorem ipsum dolor sit amet consectetur adipisicing elit. Velit, inventore nihil deleniti harum eligendi sed deserunt")


# inline func

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):

    if call.data == 'location':
        get_location(call)

    elif call.data == "get_menu":
        get_menu(call, lang)

    elif call.data == "reg":
        get_reg(call, lang)


# outline func

@ bot.message_handler(content_types=['text'])
def get_menus(message):
    global lang

    if message.text == '🇷🇺Руский':
        lang = 'ru'
        get_menu(message, lang)

    elif message.text == '🇺🇿O`zbek':
        lang = 'uz'
        get_menu(message, lang)

    elif message.text == '🇺🇸English':
        lang = 'us'
        get_menu(message, lang)

    elif (message.text == "Контакты") or (message.text == "Contactlarimiz") or (message.text == "Contacts"):
        get_contacts(message, lang)

    elif (message.text == "Наши курсы") or (message.text == "Kurslarimiz") or (message.text == "Our courses"):
        get_ourCourses(message, lang)

    elif (message.text == 'Онлайн тест') or (message.text == "Onlayn test") or (message.text == "Online test"):
        get_test(message)

    elif (message.text == 'Обратный звонок') or (message.text == "Qung`roq qilish") or (message.text == "Callback"):
        get_callback(message)

    elif (message.text == 'О нас') or (message.text == "Biza haqimizda") or (message.text == "About us"):
        get_about(message, lang)

    elif (message.text == 'Смена языка') or (message.text == "Tilini o'zgartirish") or (message.text == "Change the language"):
        get_lang(message)

    elif (message.text == '🔙Главное меню') or (message.text == "🔙Bosh menu") or (message.text == "🔙Main menu"):
        get_menu(message, lang)

    elif (message.text == 'Бытрые курсы') or (message.text == "Tezkor kurslar") or (message.text == "Fast courses"):
        fastInfo(message, lang)

    elif (message.text == 'Интинсивные курсы') or (message.text == "Intensiv kurslar") or (message.text == "Intinsive courses"):
        intensiveInfo(message, lang)

    elif (message.text == 'Лекие курсы') or (message.text == "Osan kurslar") or (message.text == "Easy courses"):
        easyInfo(message, lang)

    elif (message.text == 'Обычные курсы') or (message.text == "Oddiy kurslar") or (message.text == "Simple courses"):
        CourseInfo(message, lang)


bot.polling()
