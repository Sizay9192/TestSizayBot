import telebot

bot = telebot.TeleBot('8478649630:AAGa_0C7E3m1DGQuFoePlR42BjNZINsJ7ZY')

@bot.message_handler(comands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Привет!')

bot.polling(none_stop=True)
