# FINAL STATE MACHINE

from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message

from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from database import User as UserClass
from keyboards import kb_cancel_fsm



fsm_router = Router()

class Userr(StatesGroup):
    name = State()
    phone = State()
    address = State()
    tg_id = State()


@fsm_router.message(Command('new_user'))
async def input_name(message:Message, state:FSMContext):
    """
    Ввод имени пользователя.
    """
    await state.set_state(Userr.name)# Как только получаем команду /new_user переходим в состояние name
    await message.answer('Введите имя:',reply_markup=kb_cancel_fsm()) #Вывожу текст 

@fsm_router.message(Userr.name,F.photo)
async def new_name(message: Message, state: FSMContext): # Запускается следующий хендлер, и ждёт пока не придёт имя
    await state.update_data(name=message.text)# Отлавливает текст и записывает его в name
    await message.answer('Введите номер телефона:',reply_markup=kb_cancel_fsm()) # Выводит текст
    await state.set_state(Userr.phone) #Запускает статус phone


@fsm_router.message(Userr.phone)
async def new_phone(message: Message, state: FSMContext): # Запускается следующий хендлер, и ждёт пока не придёт телефон
    phone = message.text
    if phone.startswith('+7') and phone[1:].isdigit():
        await state.update_data(phone=phone)# Отлавливает текст и записывает его в name
        await message.answer('Введите адрес:',reply_markup=kb_cancel_fsm()) # Выводит текст
        await state.set_state(Userr.address) #Запускает статус phone
    else:
        await message.answer('Введите телефон в формате +7ХХХХХХХХХХ',reply_markup=kb_cancel_fsm())

@fsm_router.message(Userr.address)
async def new_phone(message: Message, state: FSMContext): # Запускается следующий хендлер, и ждёт пока не придёт телефон
    await state.update_data(address=message.text)# Отлавливает текст и записывает его в name
    await state.update_data(tg_id = message.from_user.id)
    our_data = await state.get_data()
    user = UserClass(our_data)
    await message.answer(f'Пользователь {our_data["name"]} сохранён!')
    await state.clear() # Сброс FSM и очистка памяти.
    