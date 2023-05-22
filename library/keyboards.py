from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from library.configs import LANGUAGES


def get_key_from_value(value):
    """Брать ключ по значению"""
    for k, v in LANGUAGES.items():
        if v == value:
            return k


def generate_languages():
    """Для кнопок выбора языка"""
    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    button = []
    for lang in LANGUAGES.values():
        btn = KeyboardButton(text=lang)
        button.append(btn)

    markup.add(*button)
    return markup
