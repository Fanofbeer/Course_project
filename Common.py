from peewee import *
from peewee import BitField
from db.models import AdminUser, User, Tag, Category, Dish,TagDish

AdminUser.delete().execute()
Dish.delete().execute()
Category.delete().execute()
Tag.delete().execute()

n=137268
r = 20
k = 0
#db = SqliteDatabase('bot.db')
#db.connect(reuse_if_open=True)


# tags =Tags.select(Tags.tag_id,Tags.name, fn.rank().over(order_by=[Tags.tag_id]).alias('rank')).order_by(Tags.tag_id.asc())
# for tag in tags:
#     print(tag.rank)
predicate = ((TagDish.tag_id==Tag.tag_id) &
             (TagDish.dish_id==1))
tags = Tag.select(Tag.tag_id,Tag.name, (~TagDish.TagDish_id.is_null().alias('check'))).join(TagDish,JOIN.LEFT_OUTER, on=((TagDish.tag_id==Tag.tag_id) & (TagDish.dish_id==1))).dicts()
#tags = TagDish.select(Tag.name, (TagDish.TagDish_id.alias('check'))).join(Tag, JOIN.FULL_OUTER).where(TagDish.dish_id==1|TagDish.tag_id.is_null()==1).order_by(Tag.tag_id).dicts()
for tag in tags:
    #print(tag.TagDish_id)
    print(tag)
    #print(tag.tag_id.Tagdish_id)
# dish = Dish.get_or_none(Dish.dish_id == 2)
# print(dish)


t =TagDish.select().dicts()
for d in t:
    print(d)

dishes = Dish.select().order_by(Dish.dish_id.asc())
for dish in dishes:
    print(dish.category_id.name)

# query = TagDish.delete()
# query.execute()
# dishes = Dish.select().join(Category)
# for dish in dishes:
#     print(dish.category_id.name)
#assert p.flags[11]
# not p.flags.is_set(11)
#
# for i in reversed(range(64)):
#     if p.flags.flag(i)==0:
#         print(0, end='')
#     else:
#         print(1, end='')
# 2^3

# if p.flags&pow(2,r)>0:
#     m=p.flags-pow(2,r)
# else:
#     m=p.flags
# print()

# for i in reversed(range(64)):
#     if m&pow(2,i)==0:
#         print(0, end='')
#     else:
#         print(1, end='')
#
# for i in range(r):
#     if m&pow(2,i)>0:
#         k+=pow(2,i)
# m=m-k
# m=m>>1
# m+=k
#
# print()
# print(k)
# for i in reversed(range(64)):
#     if m&pow(2,i)==0:
#         print(0, end='')
#     else:
#         print(1, end='')
# print()
# print(m)
