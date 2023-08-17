'''
Файл точки входа в нашего бота, вызывается из do.py
'''
import logging

# Тут должны быть используемые библиотеки для работы с telegram API
# airogram или telebot

def main():
  # Запуск логирования 
  logging.basicConfig(level=logging.INFO)
  # Вызов старта бота
  start_bot()
  # Пример логирования
  logging.info('Бот успешно запущен')
