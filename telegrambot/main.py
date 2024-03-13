import telebot
from telebot import types
import random

token = '6440690487:AAFlBscuMKsWQr6gnJdS20Op0eLKNQx3ChA'

bot = telebot.TeleBot(token)

keyboard = types.ReplyKeyboardMarkup()
btn1 = types.KeyboardButton('Play')
btn2 = types.KeyboardButton('No Play')
keyboard.add(btn1, btn2)


@bot.message_handler(commands=['start', 'game'])
def start_message(message):
    bot_message = bot.send_message(message.chat.id, 'Hello, Champion! Wanna start a game?', reply_markup=keyboard)
    bot.register_next_step_handler(bot_message, check_answer)

def check_answer(message):
    if message.text == 'Play':
        bot.send_message(message.chat.id, 'Ok, тогда лови правила игры:\nНужно угадать число, которое я загадаю в диапазоне от 1 до 10 вкючительно! У тебя будет 3 попытки! Если не угадаешь я тебя повешу! :)')
        number = random.randint(1, 10)
        print(number)
        game(message, 3, number)
    elif message.text == 'No Play':
        bot.send_message(message.chat.id, 'Нет? Пидора ответ')
    else: 
        bot_message = bot.send_message(message.chat.id, 'Wrong number. Try again!.', reply_markup=keyboard)
        bot.register_next_step_handler(bot_message, check_answer)


def game(message, attempts, number):
    message_bot = bot.send_message(message.chat.id, 'Guess number: ')
    bot.register_next_step_handler(message_bot, check_number, attempts-1, number) 

def check_number(message, attemps,number):
    if message.text == (number):
        bot.send_message (message.chat.id,'Чё дохера умный??? Поздровляю ты угадал чертила!')
    elif attemps==0:
        bot.send_message (message.chat.id,'Чё не угодал да ??? Пошёл нахуй отсюда ИШАК!')
    else:
        bot.send_message (message.chat.id,'Долбоёб ты не угодал!')
        game(message,attemps,number)
bot.polling()












