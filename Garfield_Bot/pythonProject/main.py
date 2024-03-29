import telebot

bot = telebot.TeleBot("7023360556:AAG4bp77Jc_xdCTEQZezbeaRuBwxGw92DHg")  # не публиковать


def main(message):
    bot.send_message(message.chat.id, text="Hello, world!")


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'START RUN')


@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id,
                     'help run')


@bot.message_handler(commands=['get_schedule'])
def main(message):
    bot.send_message(message.chat.id,
                     'Получить расписание')
    with open('1.xlsx', 'r') as :
        bot.send_charmap(message.chat.id, charmap)


@bot.message_handler()
def main(message):
    bot.send_message(message.chat.id, 'Я упал...')


bot.polling(none_stop=True)  # не трогать
