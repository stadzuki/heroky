import random
import time
import telebot
import requests
from telebot import types

#ДАННЫЕ, КОТОРЫЕ НУЖНО МЕНЯТЬ
bot = telebot.TeleBot('') #токен СЮДА

manager = 't.me/ххх'                           #телеграм менеджера
qiwi_numb = '+ххх'                         #номер киви
yandex_numb = 'ххх'                     #номер яндекс
card_numb = 'хххх хххх хххх хххх'                   #номер карты
btc_numb = 'ххх'     #btc кошелек

markdown = """
    *bold text*
    _italic text_
    [text](URL)
    """

#KEYBOARDS
keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('🔥Купить архив🔥','🍓Доступ в приват🍓')
keyboard1.row('Тех. поддержка👨🏻‍💻')

deliveryClub = telebot.types.ReplyKeyboardMarkup(True)
deliveryClub.row('💣ПРОБНИК| АРХИВ (50 RUB)💣', '💥АРХИВ | ИЗНОС (125 RUB)💥')
deliveryClub.row('🔥АРХИВ | ЖЕСТЬ-МИКС (200 RUB)🔥', '🍓ПОЛНЫЙ АРХИВ + ПРИВАТКА (300 RUB)🍓')
deliveryClub.row('❌Отменить действие❌')

yandexEat = telebot.types.ReplyKeyboardMarkup(True)
yandexEat.row('🍓ДОСТУП В ПРИВАТ 69 RUB🍓')
yandexEat.row('❌Отменить действие❌')

keyboard_check = telebot.types.ReplyKeyboardMarkup(True)
keyboard_check.row('Проверить оплату 💳', 'Отменить платеж ❌')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, '''Мы первые в списке лучших👍\n\n🍓Приветствуем вас в нашем телеграм канале!🍓\n💥Тут вы сможете приобрести доступ к нашей приватке💥\n💣Более 1000 довольных покупателей💣\n🔥Так же имеются возможность приобрести архив с выбором категорий🔥\n🧨Доступ можно приобрести всего за 69RUB (Навсегда)🧨\n📦Контент обновляется ежедневно📦\n💰Гарантируем возврат доступа при бане💰\n\n👨🏻‍💻Тех. поддержка и бот работает 24/7👨🏻‍💻''', reply_markup=keyboard1, parse_mode= "Markdown")

@bot.callback_query_handler(func=lambda call: call.data == 'oplata_check')
def response(call):
    bot.send_message(call.message.chat.id, 'Проверка оплаты:', reply_markup = keyboard_check)

@bot.message_handler(content_types=['text'])
def send_message(message):
    if message.text == '🔥Купить архив🔥':
        bot.send_message(message.chat.id, 'Выберите категорию архива:', reply_markup=deliveryClub)
    elif message.text == '🍓Доступ в приват🍓':
        oplata_check = telebot.types.InlineKeyboardButton('Проверить оплату', callback_data='oplata_check')
        oplata_url = telebot.types.InlineKeyboardButton('Оплатить', url='https://qiwi.com/payment/form/99?extra[%27account%27]=+79877365109&amountInteger=69&amountFraction=00&comment=79047')
        oplata = telebot.types.InlineKeyboardMarkup(row_width=1).add(oplata_url, oplata_check)
        bot.send_message(message.chat.id, "Оплатите доступ к привату\nВаша ссылка на опалту:\n\nУкажите комментарий к платежу: 79047", reply_markup = oplata)
    elif message.text == '💣ПРОБНИК| АРХИВ (50 RUB)💣':
        oplata_check = telebot.types.InlineKeyboardButton('Проверить оплату', callback_data='oplata_check')
        oplata_url = telebot.types.InlineKeyboardButton('Оплатить', url='https://qiwi.com/payment/form/99?extra[%27account%27]=+79877365109&amountInteger=50&amountFraction=00&comment=54721')
        oplata = telebot.types.InlineKeyboardMarkup(row_width=1).add(oplata_url, oplata_check)
        bot.send_message(message.chat.id, "Оплатите доступ к 💣ПРОБНИК| АРХИВ (50 RUB)💣\nВаша ссылка на оплату:\n\nУкажите комментарий к платежу: 54721", reply_markup = oplata)
    elif message.text == '💥АРХИВ | ИЗНОС (125 RUB)💥':
        oplata_check = telebot.types.InlineKeyboardButton('Проверить оплату', callback_data='oplata_check')
        oplata_url = telebot.types.InlineKeyboardButton('Оплатить', url='https://qiwi.com/payment/form/99?extra[%27account%27]=+79877365109&amountInteger=125&amountFraction=00&comment=68366')
        oplata = telebot.types.InlineKeyboardMarkup(row_width=1).add(oplata_url, oplata_check)
        bot.send_message(message.chat.id, "Оплатите доступ к 💥АРХИВ | ИЗНОС (125 RUB)💥\nВаша ссылка на оплату:\n\nУкажите комментарий к платежу: 68366", reply_markup = oplata)
    elif message.text == '🔥АРХИВ | ЖЕСТЬ-МИКС (200 RUB)🔥':
        oplata_check = telebot.types.InlineKeyboardButton('Проверить оплату', callback_data='oplata_check')
        oplata_url = telebot.types.InlineKeyboardButton('Оплатить', url='https://qiwi.com/payment/form/99?extra[%27account%27]=+79877365109&amountInteger=200&amountFraction=00&comment=21095')
        oplata = telebot.types.InlineKeyboardMarkup(row_width=1).add(oplata_url, oplata_check)
        bot.send_message(message.chat.id, "Оплатите доступ к 🔥АРХИВ | ЖЕСТЬ-МИКС (200 RUB)🔥\nВаша ссылка на оплату:\n\nУкажите комментарий к платежу: 21095", reply_markup = oplata)
    elif message.text == '🍓ПОЛНЫЙ АРХИВ + ПРИВАТКА (300 RUB)🍓':
        oplata_check = telebot.types.InlineKeyboardButton('Проверить оплату', callback_data='oplata_check')
        oplata_url = telebot.types.InlineKeyboardButton('Оплатить', url='https://qiwi.com/payment/form/99?extra[%27account%27]=+79877365109&amountInteger=300&amountFraction=00&comment=84537')
        oplata = telebot.types.InlineKeyboardMarkup(row_width=1).add(oplata_url, oplata_check)
        bot.send_message(message.chat.id, "Оплатите доступ к 🍓ПОЛНЫЙ АРХИВ + ПРИВАТКА (300 RUB)🍓\nВаша ссылка на оплату:\n\nУкажите комментарий к платежу: 84537", reply_markup = oplata)
    elif message.text == 'Проверить оплату 💳':
        bot.send_message(message.chat.id, '🔎 Поиск платежа . . .', parse_mode= "Markdown")
        time.sleep(3)
        bot.send_message(message.chat.id, '🚫 *Платеж не был найден*', parse_mode= "Markdown")
        bot.delete_message(message.chat.id, message.message_id +1,)
    elif message.text == 'Отменить платеж ❌':
        bot.send_message(message.chat.id, '❌ Платеж отменен', parse_mode='Markdown', reply_markup=keyboard1)
    elif message.text == 'Тех. поддержка👨🏻‍💻':
        bot.send_message(message.chat.id, 'У Вас возникла проблема⁉️\nОбратитесь в телеграм канал тех. поддержки 👨🏻‍💻:\nhttps://t.me/joinchat/TdIXzEvAIERRKwN0', parse_mode='Markdown', reply_markup=keyboard1)
    elif message.text == '❌Отменить действие❌':
        bot.send_message(message.chat.id, '''Мы первые в списке лучших👍\n\n🍓Приветствуем вас в нашем телеграм канале!🍓\n💥Тут вы сможете приобрести доступ к нашей приватке💥\n💣На нашем Telegram канале более 600 гб видео💣\n🔥Так же имеются возможность приобрести архив с выбором категорий🔥\n🧨Доступ можно приобрести всего за 69RUB (Навсегда)🧨\n📦Контент обновляется ежедневно📦\n💰Для такого объема это самая выгодная цена💰\n\n👨🏻‍💻Тех. поддержка и бот работает 24/7👨🏻‍💻''', reply_markup=keyboard1, parse_mode= "Markdown")
    else: bot.send_message(message.chat.id, 'Бот не отвечает на обычные сообщения', reply_markup=keyboard1)    

bot.polling()