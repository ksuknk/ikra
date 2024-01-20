import random
import telebot

TOKEN = "5873830089:AAGyk5dIkI_y48u1yPBFs7m_QI2C0teCeq0"
bot = telebot.TeleBot(TOKEN)

surname = ["друг", "брателла", "пацан", "красавчик"]
surname0 = random.choice(surname)

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, f"Привет, мой {surname0}, я Вова Адидас.\n"
                                      f"Я могу рассказать о себе. Для ознакомления с доступными командами напишите /help")

@bot.message_handler(commands=["help"])
def handle_help(message):
    bot.send_message(message.chat.id, f"Для получения личной информации обо мне, напишите команду /info\n"
                                      f"Для получения моей фотографии, напишите команду /photo\n"
                                      f"Для завершения диалога, напишите команду /end")

@bot.message_handler(commands=['info'])
def handle_info(message):
    bot.send_message(message.chat.id, f"Я Вова Адидас, основатель группировки 'Универсам'. "
                                      f"У меня есть сводный брат Марат, но его отшили, так что он теперь чушпан. "
                                      f"За руку с ним не здоровайся.")

@bot.message_handler(commands=['photo'])
def handle_photo(message):
    bot.send_photo(message.chat.id, open('media/me.jpg', 'rb'))

@bot.message_handler(commands=['end'])
def handle_end(message):
    bot.send_message(message.chat.id, f"Ну до встречи, {surname0}!")

bot.polling()