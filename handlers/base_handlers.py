import logging
import uuid
from aiogram import types


async def bot_start(msg: types.Message):
    try:
        await msg.answer(f'Привет')
    except Exception as exception:
        #await msg.answer(f'Упс. что-то пошло не так! Обратитесь к администраторам бота')
        logging.error(f'Exception : {exception}')

async def convert_string_to_uuid(msg: types.Message):
    try:
        output_msg = uuid.UUID(msg.text).hex
        await msg.answer(output_msg)
    except Exception as error:
        logging.error('Возникла ошибка {0}'.format(str(error)))
        await msg.answer("Произошла ошибка, повторите позднее")
