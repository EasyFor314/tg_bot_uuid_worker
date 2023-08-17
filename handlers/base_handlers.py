import logging
import uuid
from aiogram import types
from handlers.inline_keyboard import start_button

async def bot_start(msg: types.Message):
    try:
        await msg.answer(f'Привет, я умею взаимодействовать с UUID строкой', reply_markup=start_button )
    except Exception as exception:
        #await msg.answer(f'Упс. что-то пошло не так! Обратитесь к администраторам бота')
        logging.error(f'Exception : {exception}')

async def convert_string_to_uuid(msg: types.Message):
    try:
        output_msg = '`' + str(uuid.UUID(msg.text)) + '`'
        await msg.answer(output_msg, parse_mode= "Markdown")
    except Exception as error:
        logging.error('Возникла ошибка {0}'.format(str(error)))
        await msg.answer("Произошла ошибка, повторите позднее")

async def gen_uuid(call: types.CallbackQuery):
    try:
        output_msg = '`' + str(uuid.uuid4()) + '`'
        await call.message.answer((output_msg, parse_mode= "Markdown") ) 
    except Exception as error:
        logging.error('Возникла ошибка {0}'.format(str(error)))
        await msg.answer("Произошла ошибка, повторите позднее")
