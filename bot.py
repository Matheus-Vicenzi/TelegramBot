import telebot
from enviroment_variables import API_KEY

bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=["teste"])
def teste(msg):
    bot.send_message(msg.chat.id, "FUNCIONANDO")

bot.polling()


