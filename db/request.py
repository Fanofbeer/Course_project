""" Запросы используемые ботом для обращения к базе """

from db.models import Tag, Category, Dish, TagDish, User
from peewee import *

def id_by_name(m: Model, name: str) -> int:
    """ Возвращаем ID сущности при ее указании по точному наименованию """

    res = 0
    if (m == Tag or m == Category or m == Dish):
        res = m.select().where(m.name == name).first()
        if res==None:
            return 0
        else:
            return res.id
    return res

def all_list(m:Model):
    """ Возвращаем все значение из указанной сущности """

    res = m.select()
    return res


def dish_by_category(i: int):
    """ Возвращаем все блюда по ID категирии """

    res = Dish.select().where(Dish.category_id == i)
    return res

def dish_by_tag(i: int):
    """ Возвращаем все блюда по ID тега """

    res = Dish.select().join(TagDish).where(TagDish.tag_id==i)
    return res

def dish_wo_tag():
    """ Возвращаем блюда, у которых не указано ни одного тега """

    wtag = Dish.select().join(TagDish)
    res = Dish.select().where(Dish.id.not_in(wtag))
    return res

def dish_by_name(i: str):
    """ Возвращаем блюда по вхождению в название """
    res = [dish for dish in Dish.select() if dish.name.lower().find(i.lower()) != -1]
    return res

def categ_menu():
    """ Возвращаем позиции меню для списка категорий. Дополнительно добавляем кнопку "Назад" """

    cat = [item.name for item in all_list(Category)]
    cat.append("Назад")
    return cat

def tags_menu():
    """ Возвращаем позиции меню для списка тегов. Дополнительно добавляем кнопки "Без тегов" и "Назад"  """

    tag = [item.name for item in all_list(Tag)]
    tag.append("Без тегов")
    tag.append("Назад")
    return tag