"""Аутентификация — пропускаем сообщения только от одного Telegram аккаунта"""
from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware


class AcceseMiddleware(BaseMiddleware):
    def __init__(self, accesse_id: int):
        self.accesse_id = accesse_id
        super().__init__()

    async def on_process_massage(self, message: types.Message, _):
        if int(message.from_user.id) != int(self.accesse_id):
            await message.answer('Access Denied')
            raise CancelHandler
