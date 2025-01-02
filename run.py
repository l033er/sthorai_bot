import asyncio

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command('help'))
async def get_help(message: Message):
    await message.answer(1)

@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Это команда хелп')

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот остановлен. ✋')
