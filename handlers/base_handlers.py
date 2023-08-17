import logging
from aiogram import types


async def bot_start(msg: types.Message):
    try:
        await msg.answer(f'Привет')
    except Exception as exception:
        #await msg.answer(f'Упс. что-то пошло не так! Обратитесь к администраторам бота')
        logging.error(f'Exception : {exception}')