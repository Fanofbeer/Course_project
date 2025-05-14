from peewee import *
from werkzeug.security import generate_password_hash, check_password_hash
import datetime

db = SqliteDatabase('bot.db')

class AdminUser(Model):
    username = CharField(unique=True)
    password_hash = CharField()

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    class Meta:
        database = db

# Создаем таблицы при первом запуске
db.create_tables([AdminUser], safe=True)


class User(Model):
    user_id = BigIntegerField(unique=True)
    username = CharField(max_length=255, null=True)
    is_banned = BooleanField(default=False)
    registered_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db


db.create_tables([User])