import telebot
from os import stat

bot = telebot.TeleBot("7023360556:AAG4bp77Jc_xdCTEQZezbeaRuBwxGw92DHg")  # не публиковать
file_path = 'users'


def file_is_empty(file_path_):
    return stat(file_path_).st_size == 0


def mailing():
    if not file_is_empty(file_path):
        with open('users', 'r') as file:
            users_list = file.read()[:-1].split('\n')
            for user in users_list:
                bot.send_message(user, 'Проверка рассылки')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'START RUN, ID IS WRITING IN FILE')
    with open('users', 'r+') as file:
        if str(message.chat.id) not in file.read()[:-1].split('\n'):
            file.write(str(message.chat.id) + '\n')


@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, 'help run')


bot.polling(none_stop=True)  # не трогать
