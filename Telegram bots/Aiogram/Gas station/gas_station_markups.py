from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('🤝 The location does not work'),
            KeyboardButton('Location 📍', request_location=True),
        ],
        [
            KeyboardButton('Next ⏩')
        ]
    ],


    resize_keyboard=True
)

btn_buy = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('💴 Cash/bank card'),
            KeyboardButton('💳 Vouchers/fuel card')

        ],
        [
            KeyboardButton('Back 🔙')

        ]
    ],


    resize_keyboard=True
)


btn3 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('🛢 98'),
            KeyboardButton('🛢 95'),

        ],
        [
            KeyboardButton('🛢 92'),
            KeyboardButton('🛢 Diesel')

        ],
        [
            KeyboardButton('🛢 Gas')
        ],
        [
            KeyboardButton('Back to choosing a form of payment 🔙')
        ]
    ],


    resize_keyboard=True
)

btn4 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Lviv Region, Khodoriv, St. Shevchenko, 12-A, '
                           'gas station #20'),
            KeyboardButton('Lviv region, city of Zhydachiv, str. D. Halytskogo, 70, '
                           'gas station No. 26'),

        ],
        [
            KeyboardButton('Ivano-Frankivsk Region, Ivano-Frankivsk, '
                           'St. S. Petlyura'),
            KeyboardButton('Lviv region, village Pyatnychany, st. Lvivska, 10-A,'
                           ' gas station #25')

        ],
        [
            KeyboardButton('Lviv region, Stryi, str. Halytska, 10, gas station No. 34')
        ],
        [
            KeyboardButton('Сhoosing the type of fuel 🔙')
        ],


    ],


    resize_keyboard=True
)

btn5 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('back to Gas station  🔙'),
            KeyboardButton('Google Map'),

        ],



    ],

    resize_keyboard=True
)

btn6 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Ternopil region, Ternopil city, str. 40 S. Budnogo,'
                           ' gas station No. 75'),
            KeyboardButton('Ivano-Frankivsk region, village Khlybychyn,'
                           ' str. Zhovtneva, 39, gas station'),

        ],

        [
            KeyboardButton('Transcarpathian region, village Mizhhir\'ya,'
                           ' str. Khustska, 63, gas station No. 17'),
            KeyboardButton('Lviv region, Rava-Ruska, st. Lvivska,'
                           ' 146-A, gas station №56'),
        ],
        [
            KeyboardButton('Сhoosing the type of fuel 🔙')

        ],

    ],

    resize_keyboard=True
)
