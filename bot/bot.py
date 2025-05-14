import os
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from dotenv import load_dotenv
from db.models import User
from aiogram.types import ReplyKeyboardMarkup



load_dotenv()
logging.basicConfig(level=logging.INFO)
bot = Bot(token=os.getenv('BOT_TOKEN'))
dp = Dispatcher()

def_kb = [
    [types.KeyboardButton(text="С регистрацией")],
        [types.KeyboardButton(text="Без регистрации")]
]

#TODO: start menu - register, continue without register
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(keyboard=def_kb)
    await message.answer("Как хотите продолжить?", reply_markup=keyboard)


@dp.message(F.text.lower() == "с пюрешкой")
async def with_puree(message: types.Message):
    await message.reply("Отличный выбор!")

@dp.message(F.text.lower() == "без пюрешки")
async def without_puree(message: types.Message):
    await message.reply("Так невкусно!")
#dp.middleware.setup(LoggingMiddleware())

#TODO: already register check
@dp.message(Command("register"))
async def register_user(message: types.Message):
    if not(User.select().where(User.user_id == message.from_user.id)):
        User.create(
            user_id=message.from_user.id,
            username=message.from_user.username
        )
        await message.reply("Вы зарегистрированы!")
    else:
        await message.reply("Вы уже зарегистрированы!")


#TODO: register check
@dp.message(Command("test1"))
async def cmd_test1(message: types.Message):
    if (User.select().where(User.user_id == message.from_user.id)):
        await message.reply("Test 1")
    else:
        await message.reply("Вы не зарегистрированы")


