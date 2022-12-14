from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils.executor import start_polling

from gas_station_text import text_help, text_grafic
from gas_station_markups import *

bot = Bot(
    token='5713843573:AAHAQtppLMvKDAMt8nuOeExI_beFJH6xniQ',
    parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start(message: types.Message):
    await bot.send_message(message.chat.id, 'Chose the location', reply_markup=btn)


@dp.message_handler()
async def f(message: types.Message):
    global pay_method
    button = message.text
    pay_method = ''
    if button == 'π€ The location does not work':
        await bot.send_message(message.chat.id, text_help,
                               parse_mode=types.ParseMode.HTML,)
    elif button == 'Next β©' or button == 'Back to choosing a form of payment π':
        await bot.send_message(message.chat.id, 'Continue', reply_markup=btn_buy)
    elif button == 'Back π':
        await bot.send_message(message.chat.id, 'Back', reply_markup=btn)
    elif button == 'π΄ Cash/bank card' or button == 'π³ Vouchers/fuel card' \
            or button == 'Π‘hoosing the type of fuel π':
        pay_method = button
        await bot.send_message(message.chat.id, 'π’ Chose the fuel', reply_markup=btn3)

    elif '9' in button:
        await bot.send_message(message.chat.id, f'π³  {button} '
                               f'Choose a Gas station', reply_markup=btn4)

    elif button == 'π’ Gas' or button == 'π’ Diesel':
        await bot.send_message(message.chat.id, f'{pay_method}\n\n'
                               f'<b>Choose a Gas station :</b>', reply_markup=btn6)
    elif len(button) > 50:
        await bot.send_location(message.chat.id, 50.2700, 30.3125)
        await bot.send_message(message.chat.id,
            f'{pay_method}+\n\nβ½ {button}\n\n {text_grafic}')
    else:
        await bot.send_message(message.chat.id, '<b>I dont understand you</b>')


start_polling(dp, skip_updates=True)
