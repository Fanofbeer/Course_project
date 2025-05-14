import asyncio
from threading import Thread
from bot.bot import dp
from bot.bot import bot
from web.app import app
import os
from dotenv import load_dotenv
load_dotenv()

async def start_bot():
    await dp.start_polling(bot)

def start_web():
    app.run(host='0.0.0.0',port=os.getenv('PORT'),use_reloader=False)


if __name__ == '__main__':
    # Запуск веб-сервера в отдельном потоке
    flask_thread = Thread(target=start_web)
    flask_thread.start()
    # Запуск бота
    asyncio.run(start_bot())