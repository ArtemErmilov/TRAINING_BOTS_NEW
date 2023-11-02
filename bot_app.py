
from aiogram.types import Message, CallbackQuery
from my_token import my_token as mt

import asyncio

import os

from aiogram import Bot, Dispatcher

from handlers import handlers_router, com_start

from ihandler import callback_router

from not_use.database_old import database_connect

from database.user import User




#bot = Bot(os.getenv('TOKEN')) #Скрытие токена для PyCharm

bot = Bot(token= mt()) # Создание сущности бота.

dp = Dispatcher() # Создание сущности диспетчер.


# Вывод данных в меню по работе бота


def on_start():
    """
    Функция выполняемая при старте бота.
    """
    
    print('Бот запущен!')
    print('База данных ', end='')

    try:
        User.table()
        print('подключена.')
    except:
        print('ошибка подключения.')



def on_stop():
    """
    Функция запускается при останове бота.
    """
    print('Бот остановлен!')

# Хендлеры. Работа с отлавливанием команд из чата бота и ответами на них.


dp.include_routers(callback_router ,handlers_router) # Запуск хендлеров


async def start_bot():
    """
    Создание функции старта бота.
    Она является асинхронной.
    """

    dp.startup.register(on_start) # Запуск функции при старте бота

    dp.shutdown.register(on_stop) # Запуск функции при останове бота

    await dp.start_polling(bot) # вызов из объекта процесса старта бота


if __name__ == '__main__':
    
    asyncio.run(start_bot())



