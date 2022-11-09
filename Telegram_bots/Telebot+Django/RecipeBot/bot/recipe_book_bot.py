# Основний файл бота

from telebot import types, TeleBot
from telebot.types import InputMediaPhoto

from recipe_book_markup import *
from recipe_book_text import *

import sqlite3 as sq

from config import TOKEN

bot = TeleBot(TOKEN)


# Хендлер який реагує на команду старт
@bot.message_handler(commands=['start'])
def start_message_message(message: types.Message):
    global name_counter, flag

    # Частина FSM яка додає True у flag
    with sq.connect('../dj_bot/bot_site/db.sqlite3') as bd:

        # Роблю лічильник
        cur_count = bd.cursor()
        cur_count.execute('SELECT COUNT(*) FROM recipebook_fsm')
        fsm_count = cur_count.fetchall()

        # Додаю True у flag
        cur_flag = bd.cursor()
        cur_flag.execute(
            f"INSERT INTO recipebook_fsm VALUES ('{int(fsm_count[0][0]) + 1}',True)")
        bd.commit()

    bot.send_message(
        message.chat.id, 'Супер! Ми розпочали 😊\nТепер введіть ваше ім\'я ⌨',
        reply_markup=types.ReplyKeyboardRemove())


# Хендлер який реагує на кнопки
@bot.message_handler(content_types=['text'])
def start_message(message):
    global name, gender, first_name, last_name, user_id, username, flag, user_dict, recipe_dict

    # Частина FSM яка кладе данні з БД у змінну flag
    with sq.connect('../dj_bot/bot_site/db.sqlite3') as bd:
        # Звертаюсь до БД
        cur_fsm = bd.cursor()
        cur_fsm.execute('SELECT * FROM recipebook_fsm')
        fsm = cur_fsm.fetchall()

        # Рахую кількість данних у БД щоб зробити лічільник
        cur_count = bd.cursor()
        cur_count.execute('SELECT COUNT(*) FROM recipebook_fsm')
        fsm_count = cur_count.fetchall()

        flag = bool(fsm[int(fsm_count[0][0]) - 1][1])

    # Через if перевіряю стан FSM та зчитую ім'я
    if flag:
        name = message.text
        bot.send_message(message.chat.id,
                         f'Добре, {name}!\nВкажіть вашу стать ⚖',
                         reply_markup=markup_gender)
        first_name = message.from_user.first_name
        last_name = message.from_user.last_name
        user_id = message.from_user.id
        username = message.from_user.username

        # Частина FSM яка додає False у flag
        with sq.connect('../dj_bot/bot_site/db.sqlite3') as bd:

            # Роблю лічильник
            cur_count = bd.cursor()
            cur_count.execute('SELECT COUNT(*) FROM recipebook_fsm')
            fsm_count = cur_count.fetchall()

            # Додаю True у flag
            cur_flag = bd.cursor()
            cur_flag.execute(
                f"INSERT INTO recipebook_fsm VALUES ('{int(fsm_count[0][0]) + 1}',False)")
            bd.commit()

    # Зчитую стать
    elif message.text in list_gender or message.text == 'Назад в меню ↩':
        if message.text != 'Назад в меню ↩':
            gender = message.text
            # sqlite
            with sq.connect('../dj_bot/bot_site/db.sqlite3') as bd:
                cur_user = bd.cursor()
                cur_user.execute('SELECT * FROM recipebook_recipebook')
                user = cur_user.fetchall()

                user_dict = {i[4]: [i[5], i[6]] for i in user}
            try:
                # sqlite
                with sq.connect('../dj_bot/bot_site/db.sqlite3') as bd:
                    cur = bd.cursor()
                    cur.execute('SELECT COUNT(*) FROM recipebook_recipebook')
                    cur.execute(
                        f"INSERT INTO recipebook_recipebook  VALUES ('{user_id}','{first_name}','{last_name}','{username}','{user_id}','{name}','{gender}')")
                    bd.commit()

                with sq.connect('../dj_bot/bot_site/db.sqlite3') as bd:
                    cur_user = bd.cursor()
                    cur_user.execute('SELECT * FROM recipebook_recipebook')
                    user = cur_user.fetchall()

                    user_dict = {i[4]: [i[5], i[6]] for i in user}

            except sq.IntegrityError:
                bot.send_message(
                    message.chat.id,
                    f'Ви вже зареєстровані 😊\n\nВаша анкета:\nІм\'я: {user_dict[user_id][0]}\n'
                    f'Стать: {user_dict[user_id][1]}\nТак що продовжуємо далі',
                    reply_markup=markup_main_menu)

            else:
                bot.send_message(
                    message.chat.id,
                    f'Супер)\nСтать збережено\n\nПереходимо у головне меню 🔄',
                    reply_markup=markup_main_menu)
        else:
            bot.send_message(
                message.chat.id,
                f'Ви повернулись до головного меню 🔄',
                reply_markup=markup_main_menu)

    # "Про мене" - виводить інформацію з анкети, залишає в тому ж меню.
    elif message.text == 'Про мене ℹ':
        bot.send_message(
            message.chat.id,
            f'Вся збережена про вас інформація ℹ\n'
            f'Ім\'я: {user_dict[user_id][0]}\nСтать: {user_dict[user_id][1]}',
            reply_markup=markup_main_menu)

    # "Рецепти" - переводить у меню рецептів.
    elif message.text == 'Рецепти 🍴':
        # sqlite
        with sq.connect('../dj_bot/bot_site/db.sqlite3') as bd:
            cur = bd.cursor()
            cur.execute('SELECT * FROM recipebook_recipebook_recipe')
            recipe = cur.fetchall()

            recipe_dict = {i[1]: [i[2], i[3]] for i in recipe}

        bot.send_message(
            message.chat.id,
            'Оберіть кнопку з рецептом, який вас цікавить 🍴',
            reply_markup=ReplyKeyboardMarkup(
                row_width=2,
                resize_keyboard=True).add(
                *
                [
                    KeyboardButton(i) for i in recipe_dict.keys()]).add(
                    *
                    [
                        KeyboardButton(i) for i in exit_list]))

    # Вивід рецептів з БД
    elif message.text in recipe_dict.keys():
        media_group = []
        media_group.append(InputMediaPhoto(open(f'../dj_bot/bot_site/media/'
                                                f'{recipe_dict[message.text][1]}', 'rb'),
                                           caption=recipe_dict[message.text][0]))
        bot.send_media_group(message.chat.id, media=media_group)
    elif message.text == 'Завершити роботу 🚀':
        bot.send_message(message.chat.id, goodbye,
                         reply_markup=types.ReplyKeyboardRemove())
    # Відповідь на неправильний ввід
    else:
        bot.send_message(message.chat.id, 'Неправильний ввід 🚫')


# Відповідь на стікер
@bot.message_handler(content_types=["sticker"])
def start_message(message):
    bot.send_message(
        message.chat.id,
        'Прикольний стікер, але українською, будь ласка 😊')


# Відповідь на інші контенти
@bot.message_handler(content_types=["audio",
                                    "document",
                                    "photo",
                                    "video",
                                    "video_note",
                                    "voice",
                                    ])
def start_message(message):
    bot.send_message(message.chat.id, 'Давай все таки текстом 😏')


# Запуск бота
if __name__ == '__main__':
    bot.infinity_polling()
