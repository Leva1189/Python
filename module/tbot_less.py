import telebot
from telebot.types import Message, ReplyKeyboardMarkup, KeyboardButton

# Підключення бота за допомогою токена
bot = telebot.TeleBot("8505633431:AAHD2RdJKlB4VqPhDOePNbiDweKFsH0XArU")

# Створення масштабованої клавіатуру
my_first_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

# Додавання кнопок до клавіатури
my_first_keyboard.add(KeyboardButton("І тобі привіт"))
my_first_keyboard.add(KeyboardButton("Бувай"))

@bot.message_handler(commands=['start'])

def send_welcome(message: Message):
    #reply_markup - вказує на клавіатуру, яка буде відображатися разом із повідомленням
    bot.send_message(message.chat.id, f"Привіт! {message.from_user.username}, твоє прізвище - {message.from_user.last_name}.", 
                     reply_markup=my_first_keyboard)



# Запуск бота
bot.infinity_polling()