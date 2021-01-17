import time
import telebot
from ipynb.fs.defs.ml import is_user_alive

bot = telebot.TeleBot('token')


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, 'Привет! Назови Класс билета, Имя (одним словом), '
                                      'Пол (male/female), Возраст, Прибыл ли он с супругом (1-да, 0-нет), '
                                      'с Ребенком (1-да, 0-нет), Номер билета, его Стоимость и Порт '
                                      'пасадки, - а я предскажу, выжил ли этот пассажир на Титанике!')


@bot.message_handler(content_types=['text'])
def answer(message):
    bot.send_message(message.chat.id, 'Анализируем...')
    passenger_data = message.text.split()
    passenger_data.insert(0, 0)
    passenger_data.insert(7, ',')

    try:
        answer = is_user_alive(passenger_data)

        if int(answer):
            bot.send_message(message.chat.id, 'Везунчик! Видимо, этот пассажир успел на спасательную шлюпку.')
        elif int(answer) == 0:
            bot.send_message(message.chat.id, 'Увы, но Титаник ваш пассажир... не пережил бы.')
    except Exception:
        bot.send_message(message.chat.id, 'Вы ввели что-то не так. Проверьте порядок введенных данных.')


    do_again(message)


def do_again(message):
    bot.send_message(message.chat.id, 'Проверить живучесть кого-нибудь еще?')


if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True)
        except ():
            time.sleep(5)
