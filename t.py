from googletrans import Translator
import telebot
# from telebot import types
TOKEN = '5515701500:AAEuUSkLJrY0Dp53_XLt0ImT94aLa9rkI80'
tarjimonbot = telebot.TeleBot(token=TOKEN)


@tarjimonbot.message_handler(commands=['start'])
def salom(message):
    xabar = 'Assalomu alaykum, Tarjimon botiga xush kelibsiz.'
    xabar += '\nMatinni yuboring'
    tarjimonbot.reply_to(message, xabar)


@tarjimonbot.message_handler(func=lambda msg: msg.text is not None)

def translate(matn):
    translator = Translator()
    til = translator.detect(matn).lang
    if til == ' en ':
        return translator.translate(matn,dest='uz').text
    else:
        return translator.translate(matn,dest='en').text


def tarjima(message):
    msg = message.text
    tarjimonbot.reply_to(message, translate(msg))


tarjimonbot.polling()