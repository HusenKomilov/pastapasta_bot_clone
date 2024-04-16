from telegram import InlineKeyboardMarkup, InlineKeyboardButton


def language_inline() -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup([
        [
            InlineKeyboardButton(text="🇺🇿 O'zbekcha", callback_data="uz"),
        ],
        [
            InlineKeyboardButton(text="🇷🇺 Русский", callback_data="ru")
        ]
    ])
    return markup
