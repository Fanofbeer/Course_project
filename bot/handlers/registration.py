from aiogram import types
from db.models import User


async def register_user(message: types.Message):
    user_id = message.from_user.id
    username = message.from_user.username

    # Проверяем существующую регистрацию
    if await User.exists(user_id=user_id):
        await message.answer("✅ Вы уже зарегистрированы!")
        return

    # Создаем нового пользователя
    await User.create(
        user_id=user_id,
        username=username
    )
    await message.answer("🎉 Регистрация прошла успешно! Теперь вы можете использовать бота")