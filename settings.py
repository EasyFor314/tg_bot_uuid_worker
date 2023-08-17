'''
Файл получения констант хранимых в .env
'''
import os

BOT_TOKEN = os.getenv("BOT_TOKEN") or input("Введите BOT TOKEN:")
if not BOT_TOKEN:
    print('Вы не установили BOT_TOKEN')
    quit()
