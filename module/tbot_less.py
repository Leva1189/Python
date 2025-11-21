import telebot
from telebot.types import Message

# Підключення бота за допомогою токена
bot = telebot.TeleBot("8505633431:AAHD2RdJKlB4VqPhDOePNbiDweKFsH0XArU")


@bot.message_handler(commands=['start'])

def send_welcome(message: Message):
    bot.send_message(message.chat.id, "Привіт!")



# Запуск бота
bot.infinity_polling()