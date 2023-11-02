from aiogram import Router, F, Bot

from aiogram.types import Message, CallbackQuery

from aiogram.filters import Command

from keyboards import kb_start_reply, kb_start_inline, ikb_inline, SimpleCallBack

handlers_router = Router() # Создание сущности роутер.

from database import User

@handlers_router.message(Command('start'))
async def com_start(message:Message):
    """
    Функция выполнения команды старт.
    Запись пользователя в базу данных.
    """
    user = User(message.from_user.id)
    if(user.tg_id):
        await message.answer('Пользователь существует')
    else:
        user = User(message)
        await message.answer('Пользователь сохранён!')
        
@handlers_router.message(Command('change_n'))
async def com_change(message:Message):
    """
    Изменение имени в базе данных.
    """
    
    user = User(message.from_user.id)
    user.name = message.text.split()[-1]
    user.save()
    await message.answer('Имя пользователя изменено')

@handlers_router.message(Command('change_sn'))
async def com_change(message:Message):
    """
    Изменение фамилии в БД.
    """
    
    user = User(message.from_user.id)
    user.surname = message.text.split()[-1]
    user.save()
    await message.answer('Фамилия пользователя изменена')

@handlers_router.message(Command('del'))
async def com_change(message:Message):
    """
    Изменение фамилии в БД.
    """
    
    user = User(message.from_user.id)
    print()
    print(user)
    print()
    user.delete(user.tg_id)
    await message.answer('Пользователь удалён')





