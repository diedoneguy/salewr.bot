from email import message_from_binary_file
import config
import telebot
from telebot import types

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button= types.KeyboardButton('Корея')
    button1 = types.KeyboardButton('Германия')
    button2 = types.KeyboardButton('Франиция')
    button3 = types.KeyboardButton('Назад')
    markup.add(button,button1,button2,button3)
    bot.send_message(message.chat.id, 'Привет {0.first_name} я бот для выбоа машины'.format(message.from_user), reply_markup=markup) 

@bot.message_handler(content_types=['text'])
def get_text(message):
    if message.chat.type == 'private':
        if message.text == 'Корея':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True )
            button = types.KeyboardButton('Honda')
            button1 = types.KeyboardButton('Nissan')
            button2 = types.KeyboardButton('Touota')
            button3 = types.KeyboardButton('Назад')
            markup.add(button,button1,button2,button3)
            bot.send_message(message.chat.id,'Выберите марку:',reply_markup=markup )
        elif message.text == 'Германия':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            button = types.KeyboardButton('Mersedes')
            button1 = types.KeyboardButton('Bmw')
            button2 = types.KeyboardButton('Audi')
            button3 = types.KeyboardButton('Wolswagen')
            markup.add(button,button1,button2,button3)
            bot.send_message(message.chat.id,'Выберите марку',reply_markup=markup)
        if message.text == 'Mersedes':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button = types.KeyboardButton('CLA-class')
            button1 = types.KeyboardButton('CLS-class')
            button2 = types.KeyboardButton('E-class')
            button3 = types.KeyboardButton('C-class')
            button4 = types.KeyboardButton('B-class')
            button5 = types.KeyboardButton('G-class')
            button6 = types.KeyboardButton('Назад')
            markup.add(button,button1,button2,button3,button4,button5,button6)
            bot.send_message(message.chat.id,'Выберите класс автомобиля' , reply_markup=markup)
        elif message.text == 'Bmw':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button = types.KeyboardButton('I-8')
            button1 = types.KeyboardButton('3 series gran turismo')
            button2 = types.KeyboardButton('3-seies GT')
            markup.add(button,button1,button2)
            bot.send_message(message.chat.id,'Выберите класс автомобиля', reply_markup=markup)
        elif message.text == 'Audi':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button = types.KeyboardButton('A-4')
            button1 = types.KeyboardButton('R-8')
            button2 = types.KeyboardButton('A-8')
            button3 = types.KeyboardButton('A-3')
            markup.add(button,button1,button2,button3)
        elif message.text == 'Назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            button = types.KeyboardButton('Mersedes')
            button1 = types.KeyboardButton('Bmw')
            button2 = types.KeyboardButton('Audi')
            button3 = types.KeyboardButton('Wolswagen')
            markup.add(button,button1,button2,button3)
            bot.send_message(message.chat.id,'Выберите марку' ,reply_markup=markup)

bot.polling(non_stop = True)
