import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram import F
from aiogram.types import FSInputFile
from aiogram.types.web_app_info import WebAppInfo
import emoji
#import numpy
#import cv2
import PIL as pillow
from PIL import Image
from PIL import ImageFilter
import os


logging.basicConfig(level=logging.INFO)
bot = Bot(token="Ваш токен")
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Перейти", web_app=WebAppInfo(url="Нужная ссылка(обязательно https)"))],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer(f"Привет, {message.from_user.full_name} {emoji.emojize(':handshake:')}")
    await message.answer(f"Текст")
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("Текст", reply_markup=keyboard)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())