import telebot
import random
import phrases
import time
token = '1705468688:AAEcS61nmfN821wZ481eXNvHhhzDgGS2paE'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет,смотри что я могу.По умолчанию я в режиме обычного диалога но есть и '
                                      'спец режимы Скажи: /joke- расскажу шутку, и так каждый раз когда будешь писать это слово')


@bot.message_handler(commands=['joke'])
def joke(message):
    bot.send_message(message.chat.id, random.sample(phrases.jokes, 1))

@bot.message_handler(commands=['kick'])
def kick_user(message):
    if message.reply_to_message:
        chat_id = message.chat.id
        who_user_id = message.from_user.id
        whom_user_id = message.reply_to_message.from_user.id
        whom_user_status = bot.get_chat_member(chat_id, whom_user_id).status
        who_user_status = bot.get_chat_member(chat_id, who_user_id).status

        if who_user_status == 'creator' or who_user_status == 'administrator':
            if whom_user_status == 'administrator' or whom_user_status == 'creator':
                bot.reply_to(message, "Невозможно кикнуть администратора")
            elif whom_user_status == 'kicked' or whom_user_status == 'left':
                bot.reply_to(message, "Пользователя нет в группе")
            else:
                bot.kick_chat_member(chat_id, whom_user_id)
                bot.reply_to(message, f"Пользователь {message.reply_to_message.from_user.username} был кикнут")
        else:
            bot.reply_to(message, "Вы не являетесь администратором")


def answers_to_users_messages(message):
    flag = True  # устанавливаем флаг
    for i in phrases.recieve_nicknames:  # проходимся по всем возможным названиям переменных которые у тебя есть (переменные 'hi', 'how_you_name', 'how_are_you', 'insults',
        # 'ot_how_are_you', 'what_do_you', 'good_night', 'good_morning')
        for j in phrases.recieve[phrases.recieve_nicknames.index(
                i)]:  # для каждого названия переменной проверяем содержимое переменной ( к примеру для hi это будут 'приветик',
            # 'привет', 'hi', 'hello')

            if message.text.lower().find(j) != -1: # если содержимое переменной есть в сообщении (например 'как дела' в 'как дела?')
                bot.send_message(message.chat.id, f'{random.choice(phrases.xx(i))}') # то отправляем сообщение с рандомным текстом из переменной для ответа
                # !!!важно!!! названия перемнных ответа должны быть вида название_переменной_otv
                flag = False  # если содержимое переменной есть в сообщении то меняем значение флага, тем самым сигнализируем, что сообщение отнесенно к какой либо категории (есть в заранее добавленных вариантах ответ)
                break  # заканчиваем цикл в случае успеха
    if flag is True:  # если цикл не нашел преднаписанный сценарий
        bot.send_message(message.chat.id,
                         random.sample(phrases.general, 1))  # то отправляем рандомный смайл из переменной general


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    answers_to_users_messages(message)


bot.polling(none_stop=True)
