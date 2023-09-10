import telebot
import random
import phrases
bot = telebot.TeleBot('6379345549:AAEN-otxDH-btN0XesngJgVesO1TivJsYss')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет,смотри что я могу.По умолчанию я в режиме обычного диалога но есть и '
                                      'спец режимы Скажи: /shytka- расскажу шутку, и так каждый раз когда будешь писать это слово')
@bot.message_handler(commands=['shytka'])
def shytka(message):
       bot.send_message(message.chat.id, random.sample(phrases.jokes, 1))

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    flag = True
    for i in phrases.recieve_nicknames:
        for j in phrases.recieve[phrases.recieve_nicknames.index(i)]:
            if message.text.lower().find(j) != -1:
                bot.send_message(message.chat.id, f'{random.choice(phrases.xx(i))}')
                flag = False
                break
    if flag is True:
        bot.send_message(message.chat.id, random.sample(phrases.general, 1))

bot.polling(none_stop=True)