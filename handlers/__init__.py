from aiogram import Dispatcher
from aiogram.dispatcher.filters import CommandStart, CommandHelp, Command

from .base_handlers import bot_start, convert_string_to_uuid

def setup(dp: Dispatcher):
    dp.register_message_handler(bot_start, CommandStart())
    dp.register_message_handler(convert_string_to_uuid)
