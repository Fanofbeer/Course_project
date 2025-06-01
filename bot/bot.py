""" Описание работы Telegram-бота """
import logging
import os

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import ReplyKeyboardMarkup, Message, KeyboardButton
from dotenv import load_dotenv

from db.request import *

load_dotenv()
logging.basicConfig(level=logging.INFO)
bot = Bot(token=os.getenv('BOT_TOKEN'))
dp = Dispatcher()

def make_row_keyboard(items: list[str]) -> ReplyKeyboardMarkup:
    """ Создаем клавиатуру из текстового списка """
    kb_list = []
    for item in items:
        kb_list.append([KeyboardButton(text=item)])
    kb = ReplyKeyboardMarkup(keyboard=kb_list, resize_keyboard=True, one_time_keyboard=True)
    return kb


f_list = ["Зарегистрироваться"]
main_list = ["Блюда по категориям","Блюда по тегам","Все блюда","Поиск по названию","Выход"]

class Form(StatesGroup):
    """ Класс состояний"""
    reg = State()
    main_menu = State()
    cat = State()
    cat_dish = State()
    tag = State()
    tag_dish = State()
    all_dish = State()
    search_by_name = State()
    find_dish = State()


@dp.message(Command("start"))
async def cmd_start(message: types.Message,state: FSMContext):
    """ Старт работы с ботом при команде /start .
    Незарегистрированным пользователям предлагает зарегистрироваться.
    Зарегистрированных - перенаправляет в гравное меню"""
    if not(User.select().where(User.user_id == message.from_user.id)):
        await state.set_state(Form.reg)
        await message.answer("Нужно зарегистрироваться", reply_markup=make_row_keyboard(f_list))
    else:
        await state.set_state(Form.main_menu)
        await message.reply("Вы уже зарегистрированы!", reply_markup=make_row_keyboard(main_list))


@dp.message(Form.reg,F.text == 'Зарегистрироваться')
async def register_user(message: types.Message,state: FSMContext):
    """ Регистрация пользователя с занесением в базу данных. После регистрации перенаправляем в главное меню. """
    if not(User.select().where(User.user_id == message.from_user.id)):
        User.create(
            user_id=message.from_user.id,
            username=message.from_user.username
        )
        await message.reply("Вы зарегистрированы!",reply_markup=make_row_keyboard(main_list))
    else:
        await message.reply("Вы уже зарегистрированы!",reply_markup=make_row_keyboard(main_list))
    await state.set_state(Form.main_menu)

@dp.message(Form.main_menu)
async def main_menu(message: Message, state: FSMContext):
    """ Главное меню. Варианты взаимодействия:
    Отменить регистрацию - удаление пользователя из базы данных
    Выбор блюд по категориям - перенаправление на меню со списком категорий
    Выбор блюд по тегам - перенаправление на меню со списком тегов
    Выбор блюд из общего списка - перенаправление на меню со списком всех блюд
    Поиск блюда по названию - перенаправление в меню поиска по названию"""
    if (message.text == "Выход"):
        if (User.select().where(User.user_id == message.from_user.id)):
            User.delete().where(User.user_id == message.from_user.id).execute()
        await state.set_state(Form.reg)
        await message.reply("Регистрация отменена", reply_markup=make_row_keyboard(f_list))
    if (message.text == "Блюда по категориям"):
        await state.set_state(Form.cat)
        await message.reply("Список категорий:", reply_markup=make_row_keyboard(categ_menu()))
    if (message.text == "Блюда по тегам"):
        await state.set_state(Form.tag)
        await message.reply("Список тегов:", reply_markup=make_row_keyboard(tags_menu()))
    if (message.text == "Все блюда"):
        dish_list = [item.name for item in all_list(Dish)]
        if dish_list:
            await state.update_data(dish_list=dish_list)
            dish_list.append("Назад")
            await state.set_state(Form.all_dish)
            await message.reply("Блюда:", reply_markup=make_row_keyboard(dish_list))
        else:
            await message.reply("Блюд не найдено:", reply_markup=make_row_keyboard(main_list))
    if (message.text == "Поиск по названию"):
        await state.set_state(Form.search_by_name)
        await message.reply("Поиск по названию:", reply_markup=make_row_keyboard(["Назад"]))

@dp.message(Form.cat)
async def cat_menu(message: Message, state: FSMContext):
    """ Меню выбора котегорий. Варианты взаимодействия:
    Назад - возвращение в главное меню
    Выбор категории - перенаправление на меню выбора блюд по категории
    Ввод значений не из списка не приводит к реакции бота"""
    if (message.text == "Назад"):
        await state.set_state(Form.main_menu)
        await message.reply("Главное меню", reply_markup=make_row_keyboard(main_list))
    else:
        dish_list = [item.name for item in dish_by_category(id_by_name(Category,message.text))]
        if dish_list:
            dish_list.append("Назад")
            dish_list.append("В начало")
            await state.set_state(Form.cat_dish)
            await state.update_data(dish_list=dish_list)
            await message.reply("Блюда:", reply_markup=make_row_keyboard(dish_list))
        else:
            await message.reply("Блюд не найдено, выберите другую категорию:", reply_markup=make_row_keyboard(categ_menu()))

@dp.message(Form.cat_dish)
async def cat_dish_menu(message: Message, state: FSMContext):
    """ Меню выбора блюда по категории. Варианты взаимодействия:
    Назад - перенапралвение в меню выбора категории
    В начало - перенаправление в главное меню
    Выбор блюда - вывод информации о выбранном блюде
    Ввод значений не из списка возвращает текст 'Неизвестное блюдо'"""
    user_data = await state.get_data()
    if (message.text == "Назад"):
        await state.set_state(Form.cat)
        await message.reply("Блюда", reply_markup=make_row_keyboard(categ_menu()))
    if (message.text == "В начало"):
        await state.set_state(Form.main_menu)
        await message.reply("Главное меню", reply_markup=make_row_keyboard(main_list))
    if (message.text in user_data["dish_list"]):
        i = id_by_name(Dish, message.text)
        if i>0:
            dish = Dish.get_by_id(i)
            await message.reply(dish.name+'\n'+dish.ingredients+'\n'+dish.recipe,reply_markup=make_row_keyboard(user_data["dish_list"]))
    else:
        await message.reply('Неизвестное блюдо',reply_markup=make_row_keyboard(user_data["dish_list"]))


@dp.message(Form.tag)
async def tag_menu(message: Message, state: FSMContext):
    """ Меню выбора тега. Варианты взаимодействия:
    Назад - возвращение в главное меню
    Без тегов - перенаправление на меню выбора блюд, у которых не выбрано ни одного тега
    Выбор тега - перенаправление на меню выбора блюд по тегу
    Ввод значений не из списка не приводит к реакции бота"""
    if (message.text == "Назад"):
        await state.set_state(Form.main_menu)
        await message.reply("Главное меню", reply_markup=make_row_keyboard(main_list))
    else:
        if (message.text == "Без тегов"):
            dish_list = [item.name for item in dish_wo_tag()]
            if dish_list:
                await state.update_data(dish_list=dish_list)
                dish_list.append("Назад")
                dish_list.append("В начало")
                await state.set_state(Form.tag_dish)
                await message.reply("Блюда:", reply_markup=make_row_keyboard(dish_list))
            else:
                await message.reply("Блюд не найдено, выберите другой тег:", reply_markup=make_row_keyboard(tags_menu()))
        else:
            dish_list = [item.name for item in dish_by_tag(id_by_name(Tag,message.text))]
            if dish_list:
                await state.update_data(dish_list=dish_list)
                dish_list.append("Назад")
                dish_list.append("В начало")
                await state.set_state(Form.tag_dish)
                await message.reply("Блюда:", reply_markup=make_row_keyboard(dish_list))
            else:
                await message.reply("Блюд не найдено, выберите другой тег:", reply_markup=make_row_keyboard(tags_menu()))

@dp.message(Form.tag_dish)
async def tag_dish_menu(message: Message, state: FSMContext):
    """ Меню выбора блюда по тегу. Варианты взаимодействия:
    Назад - перенапралвение в меню выбора тега
    В начало - перенаправление в главное меню
    Выбор блюда - вывод информации о выбранном блюде
    Ввод значений не из списка возвращает текст 'Неизвестное блюдо' """
    user_data = await state.get_data()
    if (message.text == "Назад"):
        await state.set_state(Form.tag)
        await message.reply("Блюда", reply_markup=make_row_keyboard(tags_menu()))
    if (message.text == "В начало"):
        await state.set_state(Form.main_menu)
        await message.reply("Главное меню", reply_markup=make_row_keyboard(main_list))
    if (message.text in user_data["dish_list"]):
        i = id_by_name(Dish, message.text)
        if i>0:
            dish = Dish.get_by_id(i)
            await message.reply(dish.name+'\n'+dish.ingredients+'\n'+dish.recipe,reply_markup=make_row_keyboard(user_data["dish_list"]))
    else:
        await message.reply('Неизвестное блюдо',reply_markup=make_row_keyboard(user_data["dish_list"]))

@dp.message(Form.all_dish)
async def all_dish_menu(message: Message, state: FSMContext):
    """ Меню выбора их всех блюд. Варианты взаимодействия:
    Назад - перенапралвение в главное меню
    Выбор блюда - вывод информации о выбранном блюде
    Ввод значений не из списка возвращает текст 'Неизвестное блюдо' """
    user_data = await state.get_data()
    if (message.text == "Назад"):
        await state.set_state(Form.main_menu)
        await message.reply("Главное меню", reply_markup=make_row_keyboard(main_list))
    if (message.text in user_data["dish_list"]):
        i = id_by_name(Dish, message.text)
        if i>0:
            dish = Dish.get_by_id(i)
            await message.reply(dish.name+'\n'+dish.ingredients+'\n'+dish.recipe,reply_markup=make_row_keyboard(user_data["dish_list"]))
    else:
        await message.reply('Неизвестное блюдо',reply_markup=make_row_keyboard(user_data["dish_list"]))

@dp.message(Form.search_by_name)
async def search_by_name_menu(message: Message, state: FSMContext):
    """ Меню поиска по названию блюда. Варианты взаимодействия:
    Назад - перенапралвение в главное меню
    Ввода текста - поиск в названии блюда введенного текста, без учета регистра.
    При нахождении блюд перенаправление в меню выбора блюд, а при отсутствии вывод сообщение 'Блюда не найдены'"""
    if (message.text == "Назад"):
        await state.set_state(Form.main_menu)
        await message.reply("Главное меню", reply_markup=make_row_keyboard(main_list))
    else:
        dish_list = [item.name for item in dish_by_name(message.text)]
        if dish_list:
            await state.update_data(dish_list=dish_list)
            dish_list.append("Назад")
            dish_list.append("В начало")
            await state.set_state(Form.find_dish)
            await message.reply('Найденные блюда:', reply_markup=make_row_keyboard(dish_list))
        else:
            await message.reply('Блюда не найдены',reply_markup=make_row_keyboard(dish_list))

@dp.message(Form.find_dish)
async def find_dish(message: Message, state: FSMContext):
    """Меню выбора их всех блюд. Варианты взаимодействия:
    Назад - перенапралвение в меню поиска
    Выбор блюда - вывод информации о выбранном блюде
    Ввод значений не из списка возвращает текст 'Неизвестное блюдо'"""
    user_data = await state.get_data()
    if (message.text == "Назад"):
        await state.set_state(Form.search_by_name)
        await message.reply("Блюда", reply_markup=make_row_keyboard(["Назад"]))
    if (message.text == "В начало"):
        await state.set_state(Form.main_menu)
        await message.reply("Главное меню", reply_markup=make_row_keyboard(main_list))
    if (message.text in user_data["dish_list"]):
        i = id_by_name(Dish, message.text)
        if i>0:
            dish = Dish.get_by_id(i)
            await message.reply(dish.name+'\n'+dish.ingredients+'\n'+dish.recipe,reply_markup=make_row_keyboard(user_data["dish_list"]))
    else:
        await message.reply('Неизвестное блюдо',reply_markup=make_row_keyboard(user_data["dish_list"]))


