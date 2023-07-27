from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def get_default_keyboard():
    rkb = ReplyKeyboardMarkup([
        [KeyboardButton('/help')],
        [KeyboardButton('/news')],
    ], resize_keyboard=True)

    return rkb
