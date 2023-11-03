from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext



cancel_fsm_router = Router()


@cancel_fsm_router.message(F.text.casefold() == "отмена")
async def cancel_handler(message:Message, state:FSMContext) -> None:
    """
    Создание функции отмена для FSM машины.
    """
    # current_state = await state.get_state()
    # if current_state is None:
    #     return
    await state.clear()
    await message.answer('Отмена')