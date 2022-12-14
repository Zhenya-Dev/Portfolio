from random import choice, shuffle

pizza_title = {'Краща ціна':
               {'Мангеттен':
                'Подвійна порція грибів, Моцарела, Пепероні, Соус Альфредо',
                'Пепероні з томатами': 'Моцарела, Пепероні, Помідори, Соус Барбекю',
                'Шинка та гриби': 'Шинка, Гриби, Моцарела, Соус Томатний',
                'Техас':
                'Кукурудза, Цибуля, Гриби, Ковбаски баварські, Моцарела, Соус Барбекю',
                },
               'Класичні':
               {'Пепероні': 'Моцарела, Пепероні, Соус Томатний',
                'Маргарита': 'Подвійна порція моцарели, Соус Томатний',
                'Барбекю': 'Курка, Цибуля, Бекон, Гриби, Моцарела, Соус Барбекю',
                'Гриль Мікс':
                'Курка, Фрикадельки, Цибуля, Бекон, Болгарський перець, Моцарела, Соус Барбекю',
                'Карбонара':
                'Цибуля, Бекон, Шинка, Гриби, Моцарела, Соус Альфредо',
                'Кантрі-Карбонара':
                'Цибуля, Бекон, Шинка, Гриби, Моцарела, Огірки мариновані, Соус Часниковий',
                'Гавайська': 'Курка, Ананас, Моцарела, Соус Томатний',
                },
               'Дивина':
               {'Грецька': 'Фета, Оливки, Моцарела, Соус Часниковий, Тунець',
                'Тоскана': 'Курка, Фета, Моцарела, Помідори чері, Соус Альфредо, Шпинат',
                'Шпинат і Фета':
                'Фета, Оливки, Болгарський перець, Гриби, Моцарела, Помідори, Соус Альфредо, Шпинат',
                'Спайсі': 'Халапеньо, Бекон, Моцарела, Пепероні, Помідори, Соус Томатний',
                'Прованс':
                'Бергадер Блю, Шинка, Моцарела, Пепероні, Помідори, Соус Альфредо',
                'Джамайка Бомбастик':
                'Курка, Кукурудза, Халапеньо, Ананас, Болгарський перець, Гриби, Моцарела, Соус Томатний',
                'Чікен кебаб':
                'Поливка (соус Burger), Курка, Цибуля, Гриби, Моцарела, Огірки мариновані, Соус Томатний',
                'Курка-Дорблю': 'Курка, Бергадер Блю, Моцарела, Соус Альфредо',
                },
               'Преміум':
               {'Мюнхенська Делюкс':
                'Шинка, Гірчиця, Ковбаски баварські, Моцарела, Помідори, Сосиски білі, Соус Барбекю',
                'Барбекю Делюкс':
                'Фрикадельки, Цибуля, Болгарський перець, Гриби, Моцарела, Пармезан, Пепероні, Соус Барбекю',
                '4 м\'яса':
                'Бекон, Шинка, Ковбаски баварські, Моцарела, Пармезан, Пепероні, Соус Томатний',
                'П\'ять Сирів':
                'Фета, Бергадер Блю, Моцарела, Пармезан, Соус Альфредо, Чеддер',
                'Екстраваганзa':
                'Фрикадельки, Оливки, Цибуля, Болгарський перець, Шинка, Гриби, Моцарела, Пепероні, Соус Томатний',
                'Роял Чізбургер':
                'Подвійна порція стейк-м’яса яловичина, Поливка (соус Burger), Цибуля, Моцарела, Соус Барбекю',
                'Лосось Філадельфія':
                'Крем-сир Філадельфія, Лосось, Моцарела, Соус Альфредо',
                }}

pizza_cost = {'Краща ціна': {'Стандартна (30см)': 220,
                             'Середня (40см)': 260,
                             'Велика (45см)': 280, },
              'Класичні': {'Стандартна (30см)': 290,
                           'Середня (40см)': 330,
                           'Велика (45см)': 360, },
              'Дивина': {'Стандартна (30см)': 300,
                         'Середня (40см)': 340,
                         'Велика (45см)': 370, },
              'Преміум': {'Стандартна (30см)': 400,
                          'Середня (40см)': 450,
                          'Велика (45см)': 500, }}

pizza_diff = {
    'Стандартне тісто 🍕': 'Добре. Ви обрали стандартне тісто',
    'Тонке тісто 🫓': 'Добре. Піца буде зроблена на тонкому тісті з тою самою кількістью начинки.\n<b>Ціна не зміниться</b>',
    'Сирний борт 🧀': 'Добре. Піца буде зроблена з бортом з сиру Філадельфія.\n<b>До ціни буде додано: 40грн</b>',
    'Hot-dog борт 🌭': 'Добре. Піца буде зроблена з бортом з Hot-dog сосисками.\n<b>До ціни буде додано: 50грн</b>',
}

pizza_time = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ':', ' ']

pizza_amount = [str(i) for i in range(1,100)]

pizza_accept ='Ми знаходимось за адресою\n<b>Проспект Перемоги, 28, Київ📍</b>\n\nПіца буде готова за 20 хвилин 🕘'

order = 'В піцерії ви можете замовити піцу у касира\nВам її приготують протягом 20-ти хвилин\n\nМи знаходимось за адресою:\n<b>Проспект Перемоги, 28, м.Київ📍</b>'

phone = 'Бажаєте замовити піцу за телефоном?\n\n<b> Зателефонуйте за номером, вказаним нижче і вам допоможуть</b>\n\n <b>+380662426490</b>'

chose = 'Оберіть піцу, яка вам найбільше подобаєтсья і <b>натисніть на кнопку з цією піцею</b> ⬇'

rim = 'Розмір обрано. Чи хотіли б ви отримати піцу на <b>тонкому тісті</b>, чи додати <b>сирний</b> або <b>hot-dog</b> борт?'

order_time='Введіть будь ласка час, в який зробити замовлення (у форматі "09:08")'

order_way='Залишилось тільки вибрати спосіб, як ви заберете замовлення 📦'

delivery_details='Щоб уточнити деталі доставки зателефонуйте за номером\n<b>+380662426490</b>\nабо напишіть в телеграм\n<b>@zhekich_v</b>'

accept='Дякуємо за те, що обрали нашу піцерію\n\nЗамовлення підвердженно ✅'

complaint='Якщо є якісь питання, пропозиції чи скарги\nзателефонуйте за номером\n<b>+380662426490</b>\nабо напишіть в телеграм\n<b>@zhekich_v</b>'

clarify='Якщо є якісь питання, ви хочете щось додати або змінити у замовленні,\nзателефонуйте за номером\n<b>+380662426490</b>\nабо напишіть в телеграм\n<b>@zhekich_v</b>'

amount_details='Введіть кількість піц. Максимальна кількість: 99'


pizza_id=str(''.join(choice(list('01234567890')) for i in range(10)))
