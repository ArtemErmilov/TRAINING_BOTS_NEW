from .cancel import cancel_fsm_router
from .new_user import fsm_router

from aiogram import Router

all_fsm_routers = Router()
all_fsm_routers.include_routers(cancel_fsm_router, fsm_router)# cancel_fsm_router,

__all__ = ['all_fsm_routers']