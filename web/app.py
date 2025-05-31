""" Описание работы веб-админки """

import os

import requests
from dotenv import load_dotenv
from flask import Flask, render_template_string, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from flask_wtf.csrf import CSRFProtect
from peewee import fn, JOIN

from db.models import AdminUser, User, Tag, Category, Dish, TagDish
from web.forms import *

load_dotenv()

app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
csrf = CSRFProtect(app)
# Инициализация Flask-Login
login_manager = LoginManager()
login_manager.login_view = 'admin_login'
login_manager.init_app(app)


class FlaskAdminUser:
    def __init__(self, admin_user):
        self.admin_user = admin_user

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.admin_user.id)


@login_manager.user_loader
def load_user(user_id):
    """ Загрузчик пользователя """
    try:
        admin_user = AdminUser.get_by_id(user_id)
        return FlaskAdminUser(admin_user)
    except AdminUser.DoesNotExist:
        return None
@app.route('/')
def index():
    """ Главная страница для авторизации"""
    return render_template('index.html')

@app.route('/users')
def users():
    """ Вывод зарегистрированных пользователей бота без необходимости авторизации """
    users = User.select()
    return render_template_string('''
        <h1>Зарегистрированные пользователи</h1>
        <ul>
            {% for user in users %}
                <li>{{ user.username }} (ID: {{ user.user_id }})</li>
            {% endfor %}
        </ul>
    ''', users=users)

@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    """ Авторизация пользователя"""
    form = LoginForm()
    error_message = None

    if form.validate_on_submit():
        try:
            # Ищем пользователя в базе
            admin_user = AdminUser.get(AdminUser.username == form.username.data)

            # Проверяем пароль
            if admin_user.check_password(form.password.data):
                user_object = FlaskAdminUser(admin_user)
                login_user(user_object)

                # Перенаправляем на защищенную страницу
                next_page = request.args.get('next')
                return redirect(next_page or url_for('admin_dashboard'))
            else:
                error_message = "Неверный пароль"
        except AdminUser.DoesNotExist:
            error_message = "Пользователь не найден"

    return render_template(
        'admin/login.html',
        form=form,
        error=error_message
    )

@app.route('/admin/logout')
@login_required
def admin_logout():
    """ Выход из системы """
    logout_user()
    return redirect(url_for('admin_login'))


@app.route('/admin/dashboard')
@login_required
def admin_dashboard():
    """ Главная страница после авторизации"""
    total_users = User.select().count()
    return render_template('admin/dashboard.html',
                           total_users=total_users,
                           username=current_user.admin_user.username)


@app.route('/admin/users')
@login_required
def admin_users():
    """ Список загеристрированных пользователей"""
    users = User.select()
    return render_template('admin/users.html', users=users)


@app.route('/admin/send_message/<int:user_id>', methods=['GET', 'POST'])  # Добавлен GET
@login_required
def admin_send_message(user_id):
    """ Страница отправки сообщения.
        Есть возможность подставлять ID пользователя при переходе из списка пользователей"""
    user = User.get_or_none(User.user_id == user_id)
    if request.method == 'GET':
        # Показываем форму для ввода данных
        return render_template('admin/send_message.html', user = user)

    elif request.method == 'POST':
        # Обработка отправки формы
        try:
            user_id = request.form['user_id']
            message = request.form['message']

            token = os.getenv('BOT_TOKEN')
            url = f"https://api.telegram.org/bot{token}/sendMessage"

            response = requests.post(url, json={
                'chat_id': user_id,
                'text': message
            })

            if response.status_code == 200:
                return "Сообщение отправлено!"
            return f"Ошибка: {response.json()['description']}"

        except Exception as e:
            return f"Ошибка: {str(e)}"


@app.route('/admin/users/add', methods=['GET', 'POST'])
@login_required
def admin_add_user():
    """ Страница ручного добавления пользователей бота"""
    form = AddUserForm()
    if form.validate_on_submit():
        try:
            User.create(
                user_id=form.user_id.data,
                username=form.username.data
            )
            flash('Пользователь успешно добавлен', 'success')
            return redirect(url_for('admin_users'))
        except IntegrityError:
            flash('Пользователь с таким ID или именем уже существует', 'danger')
    return render_template('admin/add_user.html', form=form)


@app.route('/admin/users/<int:user_id>/edit', methods=['GET', 'POST'])
@login_required
def admin_edit_user(user_id):
    """ Страница изменения подписи пользователя бота"""
    user = User.get_or_none(User.user_id == user_id)
    if not user:
        flash('Пользователь не найден', 'danger')
        return redirect(url_for('admin_users'))

    form = EditUserForm(obj=user)
    if form.validate_on_submit():
        user.username = form.username.data
        user.save()
        flash('Данные обновлены', 'success')
        return redirect(url_for('admin_users'))
    return render_template('admin/edit_user.html', form=form, user=user)


@app.route('/admin/users/<int:user_id>/delete', methods=['POST'])
@login_required
def admin_delete_user(user_id):
    """ Удаление пользователя бота"""
    user = User.get_or_none(User.user_id == user_id)
    if user:
        user.delete_instance()
        flash('Пользователь удален', 'success')
    else:
        flash('Пользователь не найден', 'danger')
    return redirect(url_for('admin_users'))

@app.route('/admin/categories')
@login_required
def admin_categories():
    """ Страница со списком категорий"""
    categories = Category.select(Category.id,Category.name, fn.rank().over(order_by=[Category.id]).alias('rank')).order_by(Category.id.asc())
    return render_template('admin/categories.html', categories=categories)

@app.route('/admin/categories/add', methods=['POST'])
@login_required
def add_categories():
    """ Метод добавления новой категории"""
    content = request.form.get('content')
    if content:
        Category.create(name=content)
    return redirect(url_for('admin_categories'))

@app.route('/admin/categories/delete/<int:category_id>', methods=['POST'])
@login_required
def delete_categories(category_id):
    """ Метод удаления категории """
    categories = Category.get_or_none(Category.id == category_id)
    if categories:
        categories.delete_instance()
    return redirect(url_for('admin_categories'))

@app.route('/admin/dishes')
@login_required
def admin_dishes():
    """ Старница списка блюд"""
    dishes = Dish.select().order_by(Dish.id.asc())
    cats = Category.select().order_by(Category.id.asc())
    return render_template('admin/dishes.html', dishes=dishes, cats = cats)

@app.route('/admin/dishes/add', methods=['POST'])
@login_required
def add_dishes():
    """ Метод добавления нового блюда """
    name = request.form.get('name')
    ingredients = request.form.get('ingredients')
    recipe = request.form.get('recipe')
    cat = request.form.get('cat')
    if name:
        Dish.create(name=name, ingredients=ingredients, recipe=recipe, category_id= cat)
    return redirect(url_for('admin_dishes'))

@app.route('/admin/dishes/delete/<int:dishes_id>', methods=['POST'])
@login_required
def delete_dishes(dishes_id):
    """ Метод удаления блюда """
    dishes = Dish.get_or_none(Dish.id == dishes_id)
    if dishes:
        dishes.delete_instance()
    return redirect(url_for('admin_dishes'))

@app.route('/admin/tags')
@login_required
def admin_tags():
    """ Страница списка тегов """
    tags = Tag.select(Tag.id,Tag.name, fn.rank().over(order_by=[Tag.id]).alias('rank')).order_by(Tag.id.asc())
    return render_template('admin/tags.html', tags=tags)

@app.route('/admin/tags/add', methods=['POST'])
@login_required
def add_tags():
    """ Метод добавления тега"""
    content = request.form.get('name')
    if content:
        Tag.create(name=content)
    return redirect(url_for('admin_tags'))

@app.route('/admin/tags/delete/<int:tag_id>', methods=['POST'])
@login_required
def delete_tags(tag_id):
    """ Метод удаления тега """
    tags = Tag.get_or_none(Tag.id == tag_id)
    if tags:
        tags.delete_instance()
    return redirect(url_for('admin_tags'))

@app.route('/admin/tagdish_edit/<int:dish_id>')
@login_required
def admin_tagdish_edit(dish_id):
    """ Страница редактирования тегов у выбранного блюда
        Отдельно передаем те, которые сейчас выбраны"""
    dish = Dish.get_or_none(Dish.id == dish_id)
    tags = Tag.select(Tag.id,Tag.name, (~TagDish.id.is_null().alias('check'))).join(TagDish,JOIN.LEFT_OUTER, on=((TagDish.tag_id==Tag.id) & (TagDish.dish_id==dish_id)))
    return render_template('admin/tagdish_edit.html',dish=dish, tags=tags)

@app.route('/admin/tagdish_edit/save/<int:dish_id>', methods=['POST'])
@login_required
def admin_tagdish_save(dish_id):
    """ Метод сохранения тегов у блюда.
        Если галочка снята, то убираем запись из таблицы, а если галочка стоит, то проверяем была-ли она до этого и если нет, то добавляем в таблицу"""
    tags = Tag.select(Tag.id,Tag.name, (~TagDish.id.is_null().alias('check'))).join(TagDish,JOIN.LEFT_OUTER, on=((TagDish.tag_id==Tag.id) & (TagDish.dish_id==dish_id)))
    if tags:
        for tag in tags:
            i=request.form.get(tag.name)
            if i=='1':
                j=TagDish.get_or_none((TagDish.dish_id==dish_id)&(TagDish.tag_id==tag.tag_id))
                if j is None:
                    TagDish.create(dish_id=dish_id,tag_id=tag.id)
            else:
                query = TagDish.delete().where((TagDish.dish_id == dish_id) & (TagDish.tag_id == tag.id))
                query.execute()
    return redirect(url_for('admin_dishes'))