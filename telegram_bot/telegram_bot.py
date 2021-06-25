import telebot

#1863750086:AAEhckprk5OtzNMJ5w3td46LWAsah6peIHk

bot = telebot.TeleBot("1863750086:AAEhckprk5OtzNMJ5w3td46LWAsah6peIHk", parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")
@bot.message_handler(func=lambda m: True)
def echo_all(message):
    if message.text=="hello":
	    bot.reply_to(message, "hello again!")
    elif message.text == "how are you?":
        bot.reply_to(message, "I'am fine, what about you?")
    elif message.text == "fine too":
            bot.reply_to(message, "Good!")

bot.polling()