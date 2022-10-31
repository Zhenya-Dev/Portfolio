from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_btn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Замовити у боті 🍕'),
        ],
        [
            KeyboardButton('Замовити за телефоном ☎'),
            KeyboardButton('Замовити у піцерії 📍'),
        ],
    ],
    resize_keyboard=True
)

accept_btn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Підтвердити ✅'),
        ],
        [
            KeyboardButton('Відмінити ❌'),
        ],
        [
            KeyboardButton('Перевибрати спосіб отримання ⬅'),
        ],
 ],
    resize_keyboard=True, one_time_keyboard=True
)

chose_btn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Забрати у закладі 📦'),
        ],
        [
            KeyboardButton('Оформити доставку 🎁'),
        ],
        [
            KeyboardButton('Перевибрати час та кількість ⬅'),
        ],
    ],
    resize_keyboard=True, one_time_keyboard=True
)

time_btn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Зараз'),
            KeyboardButton('Обрати час 🕘')
        ],
        [
            KeyboardButton('Назад до видів ⬅'),
        ],
    ],
    resize_keyboard=True, one_time_keyboard=True
)

amount_btn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Обрати декілька'),
        ],
        [
            KeyboardButton('Залишити одну'),
        ],
    ],
    resize_keyboard=True, one_time_keyboard=True
)


def generator(pizza_list,button):
    return ReplyKeyboardMarkup(keyboard=[[KeyboardButton(i)]
                                  for i in list(pizza_list.keys()) + [button]],
                        resize_keyboard=True, one_time_keyboard=True)