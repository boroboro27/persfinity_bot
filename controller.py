"""Сервер Telegram бота, запускаемый изначально"""
import logging
import os

import aiohttp
from aiogram import Bot, Dispatcher, executor, types

import exceptions
import expenses
from middlewares import AcceseMiddleware

# задаем конфигурацию для логирования
logging.basicConfig(level=logging.INFO)

# получаем токен телеграм-бота и идентификатор пользователя из защищенного окружения
API_TOKEN = os.getenv("TELEGRAM API_TOKEN")
ACCESS_ID = os.getenv("TELEGRAM_ACCESS_ID")

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot=bot)
dp.middleware.setup(AcceseMiddleware(ACCESS_ID))


# под help расписать отдельный хэндлер
@dp.message_handler(commands=["start", "help"])
async def send_welcome(message: types.Message):
    """Отправляет приветственное сообщение и помощь по боту"""
    await message.answer(
        "Бот для учёта финансов\n\n"
        "Добавить расход: 250 такси\n"
        "Сегодняшняя статистика: /today\n"
        "За текущий месяц: /month\n"
        "Последние внесённые расходы: /expenses\n"
        "Категории трат: /categories"
    )
