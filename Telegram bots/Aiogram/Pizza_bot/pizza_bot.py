from aiogram import Bot, types
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import Dispatcher
from aiogram.utils.executor import start_polling

from config import TOKEN, ORDER_ID
from pizza_bot_info import *
from pizza_bot_markups import *


bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def f(message: types.Message):
    await bot.send_message(message.chat.id,
                           'Привіт, я бот, який допоможе тобі обрати та замовити піцу',
                           reply_markup=start_btn)


@dp.message_handler(commands='help')
async def f(message: types.Message):
    await bot.send_message(message.chat.id, complaint)


@dp.message_handler(Text(equals='Замовити у піцерії 📍'))
async def f(message: types.Message):
    await bot.send_message(message.chat.id, order)
    await bot.send_location(message.chat.id,
                            50.451559480833126, 30.466149107346293)


@dp.message_handler(Text(equals='Замовити за телефоном ☎'))
async def f(message: types.Message):
    await bot.send_message(message.chat.id, phone)


@dp.message_handler()
async def f(message: types.Message):
    global size, category, button, name, diff, \
        cost, time, time_flag, amount, amount_flag, pizza_id
    button = message.text
    try:
        if button == 'Назад ⬅':
            await bot.send_message(message.chat.id,
               'Що бажаєте обрати цього разу? 👀',
               reply_markup=start_btn)
        elif button == 'Замовити у боті 🍕' or button == 'Назад до категорій ⬅':
            await bot.send_message(message.chat.id,
               'Нижче оберіть категорію піци, яку бажаєте замовити 🍕',
               reply_markup=generator(pizza_title, 'Назад ⬅'))
        elif button in pizza_title.keys() or button == 'Назад до піц ⬅':
            if button != 'Назад до піц ⬅':
                category = button
            for i, j in pizza_title[category].items():
                photo = types.MediaGroup()
                photo.attach_photo(
                    types.InputFile(f'Photo/{i}.jpg'),
                    f"Піца: <b>{i}</b>\n\nСклад: <b>{j}</b>")
                await bot.send_media_group(message.chat.id, media=photo, )

            await bot.send_message(message.chat.id,
                                   f'Ціни в цій категорії 💰:\n')
            for i in pizza_cost[category].keys():
                await bot.send_message(message.chat.id,
                   f'<b>{i}: {pizza_cost[category][i]} грн</b>')
            await bot.send_message(message.chat.id, chose,
               reply_markup=generator(pizza_title[category], 'Назад до категорій ⬅'))
        elif button in pizza_title[category].keys() or button == 'Назад до розмірів ⬅':
            if button != 'Назад до розмірів ⬅':
                name = button
            photo = types.MediaGroup()
            photo.attach_photo(
                types.InputFile(f'Photo/{name}.jpg'),
                f'Ви обрали піцу <b>{name}</b>.\n\nОсь інгредієнти, які в неї входять:'
                f'\n<b>{pizza_title[category][name]}.</b>')
            await bot.send_media_group(message.chat.id, media=photo)
            await bot.send_message(message.chat.id,
               'Тепер оберіть, якого розміру має бути ваша піца 📏',
               reply_markup=generator(pizza_cost[category], 'Назад до піц ⬅'))
        elif button in pizza_cost[category].keys() or button == 'Назад до видів ⬅':
            if button != 'Назад до видів ⬅':
                size = button
            await bot.send_message(message.chat.id, rim,
               reply_markup=generator(pizza_diff, 'Назад до розмірів ⬅'))

        elif button in pizza_diff.keys() or button == 'Перевибрати час та кількість ⬅':
            if button != 'Перевибрати час та кількість ⬅':
                diff = button
            await bot.send_message(message.chat.id, pizza_diff[diff])
            if diff == 'Hot-dog борт 🌭':
                cost = 50
            elif diff == 'Сирний борт 🧀':
                cost = 40
            else:
                cost = 0
            await bot.send_message(message.chat.id,
               'Коли ви бажаєте отримати ваше замовлення? 🕘',
               reply_markup=time_btn)
        elif button == 'Обрати час 🕘':
            amount_flag=False
            await bot.send_message(message.chat.id, order_time)
        elif len(button)>4 and (':' in button or button=='Зараз'):
            time = button
            time_flag = False
            for i in time:
                if i not in pizza_time and button!='Зараз':
                    time_flag = True
            try:
                if time_flag or (int(time[time.find(':') + 1:]) > 59
                        or int(time[:time.find(':')]) > 23) :
                    await bot.send_message(message.chat.id,
                       'Час введено неправильно 🕘',reply_markup=time_btn)
                else:
                    await bot.send_message(message.chat.id, amount_details)
                    amount_flag = True
            except ValueError:
                await bot.send_message(message.chat.id, amount_details)
                amount_flag = True
        elif (button in pizza_amount and amount_flag) \
                or button=='Перевибрати спосіб отримання ⬅':
            if button!='Перевибрати спосіб отримання ⬅':
                amount=button
            await bot.send_message(message.chat.id,
                               f'Ваше замовлення 🍕\nПіца: <b>{name}</b> ({amount} шт) 👈')
            await bot.send_message(message.chat.id,
                               order_way, reply_markup=chose_btn)

        elif button == 'Забрати у закладі 📦' or button == 'Оформити доставку 🎁':
            if button == 'Забрати у закладі 📦':
                await bot.send_message(message.chat.id, pizza_accept)
                await bot.send_location(message.chat.id, 50.451559480833126,
                                        30.466149107346293)
            elif button == 'Оформити доставку 🎁':
                await bot.send_message(message.chat.id, delivery_details)
            photo = types.MediaGroup()
            photo.attach_photo(
                types.InputFile(f'Photo/{name}.jpg'),
                f'Ваше замолення: <b>№{pizza_id}</b>\nПіца: <b>{name}</b>\n'
                f'Склад: <b>{pizza_title[category][name]}</b>\n\n'
                f'Розмір: <b>{size}\n{diff}</b>\n\n'
                f'Ціна: <b>{int(cost+pizza_cost[category][size])*int(amount)} грн</b>'
                f'({int(cost+pizza_cost[category][size])} грн/шт)\n\n'
                f'Час: <b>{time} 🕘</b>\n\nКількість: <b>{amount} 👈</b>\n\n')
            await bot.send_media_group(message.chat.id, media=photo)
            await bot.send_message(message.chat.id, 'Підтвердити?',
                                   reply_markup=accept_btn)
        elif button == 'Підтвердити ✅':
            await bot.send_message(message.chat.id, accept, reply_markup=start_btn)
            await bot.send_message(message.chat.id, clarify)
            photo = types.MediaGroup()
            photo.attach_photo(
                types.InputFile(f'Photo/{name}.jpg'),
                f'Євгеній, нове замолення: <b>№{pizza_id}</b>\nПіца: <b>{name}</b>\n'
                f'Склад: <b>{pizza_title[category][name]}</b>\n\n'
                f'Розмір: <b>{size}\n{diff}</b>\n\n'
                f'Ціна: <b>{int(cost+pizza_cost[category][size])*int(amount)} грн</b>\n\n'
                f'{int(cost+pizza_cost[category][size])} грн шт\n\n'
                f'Час: <b>{time} 🕘</b>\n\nКількість: <b>{amount} 👈</b>\n\n')
            await bot.send_media_group(ORDER_ID, media=photo)

        elif button == 'Скасувати ❌':
            await bot.send_message(message.chat.id,
               '<b>Замовлення відмінено❌</b>\n\nВи повернулись на початок',
               reply_markup=start_btn)
        else:
            await bot.send_message(message.chat.id, 'Неправильний ввід. Введіть знову ❌')
    except NameError:
        await bot.send_message(message.chat.id, 'Неправильний ввід. Введіть знову ❌')

start_polling(dp, skip_updates=True)
