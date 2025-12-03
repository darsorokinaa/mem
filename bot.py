from telebot import TeleBot, types
import os, random

# вставь сюда свой токен
bot = TeleBot("7162771567:AAHARfNVbuCEh4E-rl1Coy4MrbiuZVciv1Y")

# команда /start — создаём меню
@bot.message_handler(commands=['start'])
def start(message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add("🚀Мем", "🎉Шутка", "💡Помощь")
    bot.send_message(message.chat.id, "Привет! Выбери, что хочешь 👇", reply_markup=kb)


# команда /meme — просто дублирует кнопку «Мем»
@bot.message_handler(commands=['meme'])
def send_meme(message):
    send_random_meme(message)


# обработка всех текстов
@bot.message_handler(content_types=['text'])
def answer(message):
    text = message.text.lower()

    # если пользователь написал "мем"
    if "мем" in text:
        send_random_meme(message)

    # если написал "шутка"
    elif "шут" in text:
        jokes = [
            "Код без ошибок — это миф 🧙",
            "Я не баг — я фича 💻",
            "Учёба — это тоже прокачка! 💪",
            "Когда всё работает — пора бояться 😅"
        ]
        bot.send_message(message.chat.id, random.choice(jokes))

    # если написал "грустно"
    elif "груст" in text:
        try:
            with open("mems/sad.jpeg", 'rb') as meme:
                bot.send_photo(message.chat.id, meme, caption="Не грусти! Вот тебе мем для настроения 💛")
        except FileNotFoundError:
            bot.send_message(message.chat.id, "Не грусти! 😊 (но у меня пока нет картинки sad.jpeg)")

    # если написал "помощь"
    elif "помощ" in text:
        bot.send_message(message.chat.id, "Напиши 'Мем' чтобы получить мем, 'Шутка' — чтобы посмеяться, 'Грустно' — если хочешь поддержку 🧡")

    # приветствие и прощание
    elif "привет" in text:
        bot.send_message(message.chat.id, "Хей! Как настроение? 😎")
    elif "пока" in text:
        bot.send_message(message.chat.id, "До встречи! 👋")

    # если бот не понял
    else:
        bot.send_message(message.chat.id, "Я тебя не понял 😅 Нажми кнопку снизу ⬇️")


# функция для отправки случайного мема
def send_random_meme(message):
    folder = "mems"  # папка с мемами
    try:
        files = os.listdir(folder)
        memes = [f for f in files if f.endswith(('.jpg', '.png', '.jpeg', '.webp'))]
        meme = random.choice(memes)
        with open(f"{folder}/{meme}", 'rb') as photo:
            bot.send_photo(message.chat.id, photo, caption="Вот твой мем дня 😄")
    except (FileNotFoundError, IndexError):
        bot.send_message(message.chat.id, "Ой 😅 Мемы не найдены! Убедись, что папка 'mems' есть и в ней есть картинки.")


# включаем бота
bot.polling(none_stop=True)
