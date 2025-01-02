import asyncio
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

load_dotenv()
TOKEN = os.getenv('TOKEN')

bot = Bot(token=TOKEN)
dp = Dispatcher()

class CommandHandler:
    @staticmethod
    @dp.message(Command('help'))
    async def get_help(message: Message):
        await message.answer('Это команда хелп! 🎋')

    @staticmethod
    @dp.message(CommandStart())
    async def cmd_start(message: Message):
        await message.answer('Привет! 👋')

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main()) 
    except KeyboardInterrupt:
        print('Бот остановлен. ✋') 
