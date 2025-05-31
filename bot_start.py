""" Запускаем бот """

import asyncio
from bot.bot import dp
from bot.bot import bot
import os
from dotenv import load_dotenv
load_dotenv()

async def start_bot():
    await dp.start_polling(bot)



if __name__ == '__main__':
    """ Запуск бота """
    asyncio.run(start_bot())