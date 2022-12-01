import telebot




bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=["teste"])
def teste(msg):
    bot.send_message(msg.chat.id, "FUNCIONANDO")

bot.polling()


