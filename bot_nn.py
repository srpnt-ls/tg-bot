import apiai
import json
import telebot
from config import TOKEN, DFKEY


bot = telebot.TeleBot(TOKEN)
keyboard1 = telebot.types.ReplyKeyboardMarkup()


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, зачем ты позвал меня?', reply_markup=keyboard1)


@bot.message_handler(content_types=['text'])
def text_message(message):
    request = apiai.ApiAI(DFKEY).text_request()
    request.lang = 'ru'
    request.session_id = 'BatlabAIBot'
    request.query = message.text
    responseJson = json.loads(request.getresponse().read().decode('utf-8'))
    response = responseJson['result']['fulfillment']['speech']
    if response:
        bot.send_message(chat_id=message.chat.id, text=response)
    else:
        bot.send_message(chat_id=message.chat.id, text='Ничего не понимаю!')


if __name__ == '__main__':
    bot.polling(none_stop=True)
