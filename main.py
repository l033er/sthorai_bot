import asyncio

from aiogram import Bot, Dispatcher

bot = Bot(token='7522553961:AAE9XKZNHTKau4R47UEnLO4ZS0FeehS6qjE')
dp = Dispatcher()


async def main():
    await dp.start_polling(bot)
    
if __name__ == '__main__':
    asyncio.run(main())
    