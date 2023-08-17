'''
Файл получения констант хранимых в .env
'''
import os

BOT_TOKEN = os.getenv("BOT_TOKEN") or input("Введите BOT TOKEN:")
if not BOT_TOKEN:
    print('Вы не установили BOT_TOKEN')
    quit()

# webhook settings
WEBHOOKS_MODE = (os.getenv('WEBHOOKS_MODE', 'True') == 'True')
# TODO Заполнить при необходиомости
WEBHOOK_URL = None
WEBHOOK_PATH = None
WEBAPP_HOST = None
WEBAPP_PORT = None