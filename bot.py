import config
import telebot
from file import Dildo, RandomMail

bot = telebot.TeleBot(config.token)


@bot.message_handler(content_types=["text"])
def msg(message):
    if message.text == '#mail':
        bot.send_message(message.chat.id, RandomMail.mail())
    elif message.text == '#status':
        bot.send_message(message.chat.id, "I'am OK !..")
    else:
        bot.send_message(message.chat.id, Dildo.answer())


if __name__ == '__main__':
    bot.polling(none_stop=True)
