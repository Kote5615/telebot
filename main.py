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
    flag = True  # устанавливаем флаг
    for i in phrases.recieve_nicknames:  # проходимся по всем возможным названиям переменных которые у тебя есть (переменные 'hi', 'how_you_name', 'how_are_you', 'insults',
        # 'ot_how_are_you', 'what_do_you', 'good_night', 'good_morning')
        for j in phrases.recieve[phrases.recieve_nicknames.index(i)]:  # для каждого названия переменной проверяем содержимое переменной ( к примеру для hi это будут 'приветик',
            # 'привет', 'hi', 'hello')
            if message.text.lower().find(j) != -1: # если содержимое переменной есть в сообщении (например 'как дела' в 'как дела?')
                bot.send_message(message.chat.id, f'{random.choice(phrases.xx(i))}') # то отправляем сообщение с рандомным текстом из переменной для ответа
            elif  message.text.lower().find(j) in mat:
                bot.delete_message(message.chat.id, message.message_id) 
                # !!!важно!!! названия перемнных ответа должны быть вида название_переменной_otv
                flag = False # если содержимое переменной есть в сообщении то меняем значение флага, тем самым сигнализируем, что сообщение отнесенно к какой либо категории (есть в заранее добавленных вариантах ответ)
                break #заканчиваем цикл в случае успеха
    if flag is True: # если цикл не нашел преднаписанный сценарий
        bot.send_message(message.chat.id, random.sample(phrases.general, 1)) #то отправляем рандомный смайл из переменной general


bot.polling(none_stop=True)
