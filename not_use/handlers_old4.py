from aiogram import Router, F, Bot

from aiogram.types import Message, CallbackQuery

from aiogram.filters import Command

from keyboards import kb_start_reply, kb_start_inline, ikb_inline, SimpleCallBack

from not_use.database_old import add_user, select_user, update_user, delete_user # Импортирование файла базы данных и функции добавления данных пользователя в базу

handlers_router = Router() # Создание сущности роутер.

@handlers_router.message(Command('start'))
async def com_start(message:Message):
    """
    Функция выполнения команды старт.
    """
    await message.answer('Привет друг!!!', reply_markup=kb_start_inline())
    # reply_markup=kb_start() - вызов кнопок из функции kb_start_inline()

@handlers_router.message(Command('hello'))# F.text == 'hello'
async def com_sta(message:Message):
    await message.answer('Выбери кто ты?', reply_markup=ikb_inline(message.from_user.first_name))
    # reply_markup=kb_start() - вызов кнопок из функции kb_start_inline()


@handlers_router.message(Command('add_user'))
async def com_add(message:Message):
    """
    Команда добавления пользователя в базу данных.
    """
    name = message.from_user.first_name # Получение данных от ТГ по имени пользователя
    surname = message.from_user.last_name # Получение фамилии от ТГ
    tg_id = message.from_user.id # Получение телеграм id от ТГ
    user = select_user(name)
    if user:
        await message.answer(f'Пользователь с именем {name} уже есть в БД!')
    else:
        add_user(name,surname,tg_id) #Добавление пользователя 
        await message.answer(f'Пользователь {name} добавлен в БД')# Текста в телеграм
    # reply_markup=kb_start() - вызов кнопок из функции kb_start_inline()

# @handlers_router.message(Command('check'))
# async def com_add(message:Message):
#     """
#     Команда вывода данных из базы данных в ТГ бота
#     """
#     tg_id = message.from_user.id # Получение телеграм id от ТГ
#     user = select_user(message.from_user.first_name,tg_id) # Получение данных из БД, вывод данных по id
    # await message.answer(str(user))# Вывод данных по запросу в ТГ чат.

# @handlers_router.message(Command('check'))
# async def com_add(message:Message):
#     """
#     Команда вывода данных из базы данных в ТГ бота
#     """
#     name = message.text.split()[1] # Вычленение имени из запроса
#     tg_id = message.from_user.id # Получение телеграм id от ТГ
#     user = select_user(name) # Получение данных из БД, вывод данных по id и имени
#     await message.answer(str(user))# Вывод данных по запросу в ТГ чат.
   
@handlers_router.message(F.text.startswith('найти'))
async def com_add(message:Message):
    """
    Поиск по тексту.
    """
    name = message.text.split()[1] # Вычленение имени из запроса
    tg_id = message.from_user.id # Получение телеграм id от ТГ
    user = select_user(name) # Получение данных из БД, вывод данных по id и имени
    await message.answer(str(user))# Вывод данных по запросу в ТГ чат.
   
@handlers_router.message(F.text.startswith('сменить имя'))
async def com_update_name(message:Message):
    """
    Поиск по тексту.
    """
    old_name = message.from_user.first_name
    name = message.text.split()[-1] # Вычленение имени из запроса
    tg_id = message.from_user.id # Получение телеграм id от ТГ
    update_user(tg_id,name) # Изменение в базе данных
    await message.answer(f'Пользователь {old_name} сменил имя на {name}')# Вывод данных по запросу в ТГ чат.

@handlers_router.message(F.text.startswith('убить себя'))
async def com_delete_name(message:Message):
    """
    Удаление пользователя из базы данных.
    """
    old_name = message.from_user.first_name
    tg_id = message.from_user.id # Получение телеграм id от ТГ
    delete_user(tg_id) # Изменение в базе данных
    await message.answer(f'Пользователь {old_name} удалён из базы данных.')# Вывод данных по запросу в ТГ чат.
   