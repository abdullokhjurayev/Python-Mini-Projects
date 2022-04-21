from transliterate import to_latin, to_cyrillic
import telebot

TOKEN = "" # Your bots token
bot = telebot.TeleBot(TOKEN, parse_mode=None)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    answer = "Hello, Welcome!"
    answer += "\nEnter the text:"
    bot.reply_to(message, answer)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg = message.text
    if msg.isascii():
        answer = to_cyrillic(msg)
    else:
        answer = to_latin(msg)
    bot.reply_to(message, answer)


bot.polling()
