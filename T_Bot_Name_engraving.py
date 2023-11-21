from create_name import *
from create_name_circle import *
from create_squared_name import FontCreation2
import telebot

bot = telebot.TeleBot('6409225370:AAFjU9gXb9-Vcswj18yYrfu6GcejNwiJGbc')


@bot.message_handler(commands=['start'])
def start(message):
    mess = (f'Привет, <b><u>{message.from_user.first_name} </u></b>\nНажми сюда /Create для '
            f'создания именной гравировки')
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler(commands=['Create'])
def create(message):
    bot.send_message(message.chat.id, "Введите имя:")


@bot.message_handler(content_types=['text'])
def handle_text_message(message):
    name = message.text

    creat_name(name, font_path, output_image)
    output_path = open(output_image, 'rb')
    bot.send_photo(message.chat.id, output_path)

    creat_name2(name, font_path2, output_image)
    output_path2 = open(output_image, 'rb')

    mess = ('\nВ какой форме вы хотите увидеть своё имя:\n'
            '1. Круг         ◯\n'
            '2. Квадрат  ☐\n'
            'Для обозначения укажите цифру')

    bot.send_photo(message.chat.id, output_path2)
    msg = bot.send_message(message.chat.id, mess)
    bot.register_next_step_handler(msg, handle_text_message2, name)


def handle_text_message2(message, name):
    qwd = message.text
    if qwd == "1":
        cd = FontCreation(name, font_path, output_image2)
        cd.create_name_engraving()

        output_path = open(output_image2, 'rb')
        bot.send_photo(message.chat.id, output_path)

        cd.create_name_engraving2()
        output_path2 = open(output_image2, 'rb')
        bot.send_photo(message.chat.id, output_path2)

    elif qwd == "2":
        cs = FontCreation2(name, font_path, output_image3)
        cs.name_square()

        output_path = open(output_image3, 'rb')
        bot.send_photo(message.chat.id, output_path)

        cs.name_square2()
        output_path2 = open(output_image3, 'rb')
        bot.send_photo(message.chat.id, output_path2)
    else:
        mes = bot.send_message(message.chat.id, ('Введите число'))
        bot.register_next_step_handler(mes, handle_text_message2, name)


bot.polling(none_stop=True)
