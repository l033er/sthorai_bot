import asyncio
from loguru import logger

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import Message

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Привет!')

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    logger.add("file.log", level="INFO") 
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info('Stopping the bot...')
