"""
Создание базы данных и описание таблиц
Создает указанные таблицы при их отсутствии
"""

from peewee import *
from werkzeug.security import generate_password_hash, check_password_hash
import datetime

db = SqliteDatabase('bot.db',pragmas={'foreign_keys': 1})

class AdminUser(Model):
    """Класс для пользователей веб-админки"""
    username = CharField(unique=True)
    password_hash = CharField()

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    class Meta:
        database = db

class User(Model):
    """ Класс для зарегистрированных пользователей бота """
    user_id = BigIntegerField(unique=True)
    username = CharField(max_length=255, null=True)
    registered_at = DateTimeField(default=datetime.datetime.now)
    class Meta:
        database = db

class Tag(Model):
    """ Класс для списка тегов"""
    id = AutoField()
    name = CharField(unique=True)
    class Meta:
        database = db

class Category(Model):
    """ Класс для списка категорий """
    id = AutoField()
    name = CharField(unique=True)
    class Meta:
        database = db

class Dish(Model):
    """ Класс для списка блюд"""
    id = AutoField()
    name = CharField(unique=True)
    category_id = ForeignKeyField(Category, backref='dish')
    ingredients = TextField(null=True)
    recipe = TextField(null=True)
    class Meta:
        database = db

class TagDish(Model):
    """ Класс для связки блюда с тегами"""
    id = AutoField()
    dish_id = ForeignKeyField(Dish, backref='tagdish', on_delete='CASCADE')
    tag_id = ForeignKeyField(Tag, backref='tagdish',  on_delete='CASCADE')
    class Meta:
        database = db


db.create_tables([AdminUser,User,Tag,Category,Dish,TagDish], safe=True)