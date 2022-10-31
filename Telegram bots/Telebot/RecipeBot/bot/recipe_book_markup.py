# Файл з кнопками

from telebot.types import ReplyKeyboardMarkup, KeyboardButton

from recipe_book_text import *


def markup(list):
    markup_btn = ReplyKeyboardMarkup(
        row_width=2,
        resize_keyboard=True,
        one_time_keyboard=True)
    markup_btn.add(*[KeyboardButton(i) for i in list])
    return markup_btn


markup_gender = markup(list_gender)

markup_main_menu = markup(main_menu)
