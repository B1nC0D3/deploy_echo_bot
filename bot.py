from telebot import TeleBot
from config import TOKEN


bot = TeleBot(TOKEN)


@bot.message_handler(content_types=['text'])
def echo(message):
    bot.send_message(message.chat.id, message.text)


bot.polling()
