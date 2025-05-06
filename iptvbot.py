import telebot
from telebot import types

bot = telebot.TeleBot("7929099756:AAH3x2IeqQTbktuKu20Ab87csVL3BnfHrtM")
ADMIN_ID = 913181906  # Telegram ID владельца для приёма заявок

# Хранилище для анкет
user_data = {}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("📺 Хочу подключиться")
    btn2 = types.KeyboardButton("📃 Категории каналов")
    btn3 = types.KeyboardButton("❓ Частые вопросы")
    btn4 = types.KeyboardButton("📦 Smart TV Box")
    btn5 = types.KeyboardButton("💬 Отзывы клиентов")
    btn6 = types.KeyboardButton("📄 Оставить заявку")
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6)

    welcome_text = (
        "👋 Привет! Добро пожаловать в *IPTV за $1 в месяц!*\n\n"
        "📡 Более *4000 каналов* со всего мира:\n"
        "🇷🇺 Россия, 🇰🇿 Казахстан, 🇺🇸 США, 🇬🇧 UK, 🇹🇷 Турция и другие\n\n"
        "🎬 Кино, 🎉 шоу, 🎮 спорт, 🎧 музыка, 🎨 детские и даже 😏 взрослые каналы\n\n"
        "Без VPN. Без подписок. Всего *$1 в месяц*. Оплата по Telegram 💸\n\n"
        "👇 Выберите интересующий пункт меню."
    )
    bot.send_message(message.chat.id, welcome_text, reply_markup=markup, parse_mode='Markdown')

@bot.message_handler(func=lambda m: m.text == "📺 Хочу подключиться")
def connect_user(message):
    bot.send_message(message.chat.id, "🎉 Напиши нам в Telegram 👉 @[написать в Telegram](https://t.me/Yerzhan2403)")

@bot.message_handler(func=lambda m: m.text == "📃 Категории каналов")
def send_categories(message):
    text = (
        "*📺 Категории каналов в подписке:*\n\n"
        "📰 Новости\n🎬 Кино\n🎧 Музыка\n📚 Познавательные\n👶 Детские\n😂 Развлекательные\n⚽️ Спорт\n🎭 Другие\n\n"
        "🔞 Взрослые (18+)\n📀 HD и HD Original\n📺 4K каналы\n\n"
        "*🌍 Языковые и региональные:*\n"
        "🇷🇺 Русские\n🇺🇸 USA\n🇰🇿 Казахстан\n🇺🇦 Українські\n🇧🇾 Беларуская\n🇦🇿 Азербайджан\n🇹🇯 Точик\n🇺🇿 O’zbek\n🇲🇩 Moldovenească\n🇬🇪 ქართული\n🇦🇲 Հայկական\n🇮🇱 Израильские\n🇹🇷 Türk"
    )
    bot.send_message(message.chat.id, text, parse_mode='Markdown')

@bot.message_handler(func=lambda m: m.text == "❓ Частые вопросы")
def send_faq(message):
    faq_text = (
        "*💰 Сколько стоит подписка?*\n"
        "— Всего $1 в месяц!\n\n"
        "*💸 Сколько стоит подключение?*\n"
        "— От $10 до $20, в зависимости от устройства.\n\n"
        "*🌍 Где работает IPTV?*\n"
        "— В любой стране.\n\n"
        "*📺 Как смотреть?*\n"
        "— Через приложение на Smart TV (мы настраиваем дистанционно), а также на телефоне, планшете или приставке.\n\n"
        "*📦 Что входит в подписку?*\n"
        "— 4000+ каналов: кино, спорт, детские, 18+, HD/4K и др.\n\n"
        "*💳 Как платить абонентскую плату?*\n"
        "— В личном кабинете. Принимаются любые карты.\n\n"
        "*📶 Что нужно для работы каналов?*\n"
        "— Стабильный интернет от 8 Мбит/с.\n\n"
        "*🔢 Сколько устройств можно подключить?*\n"
        "— 2 одновременно. Плата не меняется."
    )
    bot.send_message(message.chat.id, faq_text, parse_mode='Markdown')

@bot.message_handler(func=lambda m: m.text == "📦 Smart TV Box")
def smart_box_info(message):
    text = (
        "*📦 Smart TV Box*\n\n"
        "Если у телевизора *нет функции Smart TV* — не проблема!\n\n"
        "Мы предлагаем *приставку с готовым IPTV*. Подключи к Wi-Fi и смотри 4000+ каналов.\n\n"
        "✅ Работает на старых ТВ\n"
        "✅ Не нужно покупать новый Smart TV\n"
        "✅ YouTube, кинотеатры, IPTV — всё в одной коробке\n"
        "✅ Готова к использованию\n"
        "✅ Пульт в комплекте\n"
        "✅ Full HD / 4K\n"
        "✅ Работает в любой стране, где есть Wi-Fi или проводной интернет 🌍\n\n"
        "💰 Стоимость: *по запросу*\n"
        "📲 Заказать 👉 [написать в Telegram](https://t.me/Yerzhan2403)"
    )
    bot.send_message(message.chat.id, text, parse_mode='Markdown')

@bot.message_handler(func=lambda m: m.text == "💬 Отзывы клиентов")
def show_reviews(message):
    text = (
        "*💬 Отзывы клиентов:*\n\n"
        "🧔 Алексей 🇷🇺\n“Плачу 1 доллар, а каналов больше, чем в кабельном ТВ. Уже 4 месяца — всё работает идеально.”\n\n"
        "👩 Алия 🇰🇿\n“Брала приставку с собой в отпуск — подключилось за 3 минуты. Мужу теперь даже Netflix не нужен 😄”\n\n"
        "🧔‍♂️ Тимур 🇦🇪\n“Работает в Дубае без проблем, даже на старом телевизоре. Рекомендую друзьям.”"
    )
    bot.send_message(message.chat.id, text, parse_mode='Markdown')

# Анкета клиента
@bot.message_handler(func=lambda m: m.text == "📄 Оставить заявку")
def ask_name(message):
    user_data[message.chat.id] = {}
    bot.send_message(message.chat.id, "📛 Как вас зовут?")
    bot.register_next_step_handler(message, ask_country)

def ask_country(message):
    user_data[message.chat.id]['name'] = message.text
    bot.send_message(message.chat.id, "🌍 В какой стране вы находитесь?")
    bot.register_next_step_handler(message, ask_device)

def ask_device(message):
    user_data[message.chat.id]['country'] = message.text
    bot.send_message(message.chat.id, "📺 Какое у вас устройство? (Smart TV + модель, обычный телевизор, телефон и т.д.)")
    bot.register_next_step_handler(message, ask_internet)

def ask_internet(message):
    user_data[message.chat.id]['device'] = message.text
    bot.send_message(message.chat.id, "📶 Есть ли у вас стабильный интернет не ниже 8 Мбит/с? (Да/Нет)")
    bot.register_next_step_handler(message, finish_form)

def finish_form(message):
    user_data[message.chat.id]['internet'] = message.text
    data = user_data[message.chat.id]
    text = (
        f"📝 *Новая заявка на IPTV:*\n\n"
        f"👤 Имя: {data['name']}\n"
        f"🌍 Страна: {data['country']}\n"
        f"📺 Устройство: {data['device']}\n"
        f"📶 Интернет: {data['internet']}"
    )
    bot.send_message(ADMIN_ID, text, parse_mode='Markdown')
    bot.send_message(message.chat.id, "✅ Спасибо! Ваша заявка отправлена. Мы скоро свяжемся с вами.")

bot.polling()
