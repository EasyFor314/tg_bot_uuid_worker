from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

keyboard=[
    InlineKeyboardButton(text='Сгенерировать UUID', callback_data="gen_uuid"),
]
start_button = InlineKeyboardMarkup(row_width=1)
start_button.add(*keyboard)