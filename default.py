from telegram import ReplyKeyboardMarkup, KeyboardButton


def send_contact() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup([[
        KeyboardButton(text="Raqamni jo'natish", request_contact=True)
    ]], resize_keyboard=True, one_time_keyboard=True)


def main_menyu() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        [
            [
                KeyboardButton(text="🍴 Menyu"),
                KeyboardButton(text="📥 Savat")
            ],
            [
                KeyboardButton(text="KAFE LOKATSIYASI"),
                KeyboardButton(text="🚀 Buyurtma haqida")
            ],
            [
                KeyboardButton(text="✍️ Fikr bildirish"),
                KeyboardButton(text="☎️ Kontaktlar")
            ],
            [
                KeyboardButton(text="⚙️ Sozlamalar")
            ]
        ],
        resize_keyboard=True
    )


def send_location() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup([[
        KeyboardButton(text="Manzilni jo'natish", request_location=True)
    ]], resize_keyboard=True, one_time_keyboard=True)


def menu_button() -> ReplyKeyboardMarkup:
    markup = ReplyKeyboardMarkup(
        [
            [
                KeyboardButton(text="📥 Savat")
            ],
            [
                KeyboardButton(text="Pasta"),
                KeyboardButton(text="Qo'shimchalar")
            ],
            [
                KeyboardButton(text="Salatlar"),
                KeyboardButton(text="🆕 Taomlar")
            ],
            [
                KeyboardButton(text="Sovuq ichimliklar"),
                KeyboardButton(text="🆕 Tomato seti")
            ],
            [
                KeyboardButton(text="2 KISHILIK SET"),
                KeyboardButton(text="🆕 Ravioli ikki kishilik")
            ],
            [
                KeyboardButton(text="🔥 Kombo 4 kishilik"),
                KeyboardButton(text="😍 KIDS MENU")
            ],
            [
                KeyboardButton(text="🏘 Bosh menu")
            ]
        ], resize_keyboard=True, one_time_keyboard=True)
    return markup


def comment_button() -> ReplyKeyboardMarkup:
    markup = ReplyKeyboardMarkup([
        [
            KeyboardButton(text="😊Hammasi yoqdi ❤️"),
        ],
        [
            KeyboardButton(text="☺️Yaxshi ⭐️⭐️⭐️⭐️"),
        ],
        [
            KeyboardButton(text="😐Yoqmadi ⭐️⭐️⭐️"),
        ],
        [
            KeyboardButton(text="🙁Yomon ⭐️⭐️"),
        ],
        [
            KeyboardButton(text="😤Juda yomon 👎"),
        ],
        [
            KeyboardButton(text="🏘 Bosh menu")
        ]
    ], resize_keyboard=True, one_time_keyboard=True)
    return markup


def settings_button() -> ReplyKeyboardMarkup:
    markup = ReplyKeyboardMarkup([
        [
            KeyboardButton(text="🌐 Tilni tanlash"),
        ],
        [
            KeyboardButton(text="📱 Raqamni o'zgartirish")
        ],
        [
            KeyboardButton(text="🏘 Bosh menu")
        ]
    ], resize_keyboard=True, one_time_keyboard=True)
    return markup


def backet_button() -> ReplyKeyboardMarkup:
    markup = ReplyKeyboardMarkup([
        [
            KeyboardButton(text="🏘 Bosh menu"),
            KeyboardButton(text="🔄 Tozalash")
        ],
        [
            KeyboardButton(text="🛍 Пакет")
        ],
        [
            KeyboardButton(text="🚖 Buyurtma berish")
        ]
    ], resize_keyboard=True)
    return markup


def placing_button() -> ReplyKeyboardMarkup:
    markup = ReplyKeyboardMarkup([
        [
            KeyboardButton(text="🚖 Yetkazib berish")
        ],
        [
            KeyboardButton(text="🏃 Olib ketish")
        ],
        [
            KeyboardButton(text="🏘 Bosh menu")
        ]
    ], resize_keyboard=True)
    return markup
