from aiogram import types

async def start_command(message: types.Message):
    await message.answer("👋 Добро пожаловать! Вот список доступных команд...")