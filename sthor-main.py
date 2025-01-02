import asyncio
from aiogram import Bot


loop = asyncio.get_event_loop()
bot = Bot('TOKEN', loop)

async def main():
    bot_info = await bot.get_me()
    print(bot_info.username)


if __name__ == '__main__':
    try:
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        loop.stop()