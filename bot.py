'''
Файл точки входа в нашего бота, вызывается из do.py
'''
import logging
import settings
import asyncio

from aiogram import Bot, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import Dispatcher
from aiogram.utils.executor import start_webhook, start_polling
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import exceptions, executor

bot = Bot(token=settings.BOT_TOKEN)
mGlobalDisp = Dispatcher(bot, storage=MemoryStorage())
mGlobalDisp.middleware.setup(LoggingMiddleware())

async def set_default_commands():
    '''Установить возможные команды для бота'''
    return

async def on_startup(mDisp):
    logging.info('Настройка перед запуском')

    await set_default_commands()

    import handlers
    # Установим обработчики
    handlers.setup(mGlobalDisp )

    logging.info('Starting connection. ')
    if settings.WEBHOOKS_MODE is True:
        result = await bot.set_webhook(settings.WEBHOOK_URL, drop_pending_updates=True)
        if result:
            logging.warning('Хук успешно установлен.')
        else:
            logging.error('Хук не удалось установить.')

async def on_shutdown(mDisp):
    '''При выключении бота'''
    logging.warning('Bye! Shutting down webhook connection')
    # Сообщение для админов
    #await bot.send_message(settings.admins[0], '<b>Статус бота: Выключен</b>', parse_mode="HTML")


def main():
    '''Основная функция запуска бота'''
    logging.basicConfig(level=logging.INFO)
    if settings.WEBHOOKS_MODE is True:
        logging.info('Запуск на веб хуках')
        start_webhook(
            dispatcher=mGlobalDisp,
            webhook_path=settings.WEBHOOK_PATH,
            skip_updates=True,
            on_startup=on_startup,
            on_shutdown=on_shutdown,
            host=settings.WEBAPP_HOST,
            port=settings.WEBAPP_PORT,
        )
    else:
        logging.info('Запуск на пулинге')
        start_polling(
            dispatcher=mGlobalDisp,
            skip_updates=True,
            on_startup=on_startup)
