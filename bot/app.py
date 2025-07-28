from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import asyncio
import os

load_dotenv()

bot = Bot(token=os.getenv("TELEGRAM_TOKEN"))
dp = Dispatcher()

@dp.message(Command('start'))
async def start(message):
    await message.answer("Добро пожаловать в QuizMaster!")

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())