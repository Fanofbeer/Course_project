""" Файл для проверки и валидации запросов и данных"""

from db.request import *

# AdminUser.delete().execute()
# Dish.delete().execute()
# Category.delete().execute()
# Tag.delete().execute()
# User.delete().execute()

dish = Category.select().dicts()
for d in dish:
    print(d)


dish_list = [item.name for item in dish_by_category(id_by_name(Category,'Бульоны'))]
for d in dish_list:
    print(d)

for d in categ_menu():
    print(d)