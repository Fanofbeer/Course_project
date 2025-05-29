from flask import Flask, render_template_string, render_template, request,redirect, url_for, jsonify,flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from db.models import AdminUser, User, Tag, Category, Dish, TagDish
from flask_wtf.csrf import CSRFProtect
import requests
import os

from dotenv import load_dotenv
from web.forms import *
from peewee import fn,JOIN
load_dotenv()

app = Flask(__name__, template_folder='templates')


SECRET_KEY = os.getenv('SECRET_KEY')
app.config['SECRET_KEY'] = SECRET_KEY
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
    try:
        admin_user = AdminUser.get_by_id(user_id)
        return FlaskAdminUser(admin_user)
    except AdminUser.DoesNotExist:
        return None
@app.route('/')
def index():
    return render_template('index.html')
    # return render_template_string('''
    #     <h1>Веб-интерфейс бота</h1>
    #     <p>Статус бота: Активен</p>
    # ''')
@app.route('/users')
def users():
    users = User.select()
    return render_template_string('''
        <h1>Зарегистрированные пользователи</h1>
        <ul>
            {% for user in users %}
                <li>{{ user.username }} (ID: {{ user.user_id }})</li>
            {% endfor %}
        </ul>
    ''', users=users)

@login_manager.user_loader
def load_user(user_id):
    try:
        admin_user = AdminUser.get_by_id(user_id)
        return FlaskAdminUser(admin_user)
    except AdminUser.DoesNotExist:
        return None
@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
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
    logout_user()
    return redirect(url_for('admin_login'))


@app.route('/admin/dashboard')
@login_required
def admin_dashboard():
    total_users = User.select().count()
    return render_template('admin/dashboard.html',
                           total_users=total_users,
                           username=current_user.admin_user.username)


@app.route('/admin/users')
@login_required
def admin_users():
    users = User.select()
    return render_template('admin/users.html', users=users)


@app.route('/admin/send_message/<int:user_id>', methods=['GET', 'POST'])  # Добавлен GET
@login_required
def admin_send_message(user_id):
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
    categories = Category.select(Category.category_id,Category.name, fn.rank().over(order_by=[Category.category_id]).alias('rank')).order_by(Category.category_id.asc())
    return render_template('admin/categories.html', categories=categories)

@app.route('/admin/categories/add', methods=['POST'])
@login_required
def add_categories():
    content = request.form.get('content')
    if content:
        Category.create(name=content)
    return redirect(url_for('admin_categories'))

@app.route('/admin/categories/delete/<int:categories_id>', methods=['POST'])
@login_required
def delete_categories(category_id):
    categories = Category.get_or_none(Category.category_id == category_id)
    if categories:
        categories.delete_instance()
    return redirect(url_for('admin_categories'))

@app.route('/admin/dishes')
@login_required
def admin_dishes():
    dishes = Dish.select().order_by(Dish.dish_id.asc())
    cats = Category.select().order_by(Category.category_id.asc())
    return render_template('admin/dishes.html', dishes=dishes, cats = cats)

@app.route('/admin/dishes/add', methods=['POST'])
@login_required
def add_dishes():
    name = request.form.get('name')
    ingredients = request.form.get('ingredients')
    recipe = request.form.get('recipe')
    cat = request.form.get('cat')
    if name:
        Dish.create(name=name, ingredients=ingredients, recipe=recipe, category_id= cat)
    return redirect(url_for('admin_dishes'))

@app.route('/admin/dishes/delete/<int:categories_id>', methods=['POST'])
@login_required
def delete_dishes(dishes_id):
    dishes = Dish.get_or_none(Dish.dish_id == dishes_id)
    if dishes:
        dishes.delete_instance()
    return redirect(url_for('admin_dishes'))

@app.route('/admin/tags')
@login_required
def admin_tags():
    tags = Tag.select(Tag.tag_id,Tag.name, fn.rank().over(order_by=[Tag.tag_id]).alias('rank')).order_by(Tag.tag_id.asc())
    return render_template('admin/tags.html', tags=tags)

@app.route('/admin/tags/add', methods=['POST'])
@login_required
def add_tags():
    content = request.form.get('name')
    if content:
        Tag.create(name=content)
    return redirect(url_for('admin_tags'))

@app.route('/admin/tags/delete/<int:tag_id>', methods=['POST'])
@login_required
def delete_tags(tag_id):
    tags = Tag.get_or_none(Tag.tag_id == tag_id)
    if tags:
        tags.delete_instance()
        TagDish.delete().where(TagDish.tag_id == tags).execute()
    return redirect(url_for('admin_tags'))

@app.route('/admin/tagdish_edit/<int:dish_id>')
@login_required
def admin_tagdish_edit(dish_id):
    dish = Dish.get_or_none(Dish.dish_id == dish_id)
    tags = Tag.select(Tag.tag_id,Tag.name, (~TagDish.TagDish_id.is_null().alias('check'))).join(TagDish,JOIN.LEFT_OUTER, on=((TagDish.tag_id==Tag.tag_id) & (TagDish.dish_id==dish_id)))
    #tags = Tag.select().join(TagDish, JOIN.LEFT_OUTER, on=(Tag.tag_id==TagDish.tag_id)).where(TagDish.dish_id == dish_id)
    #tags = TagDish.select().join(Tag, on=(TagDish.tag_id == Tag.tag_id)).where(TagDish.dish_id == dish_id)

    return render_template('admin/tagdish_edit.html',dish=dish, tags=tags)

@app.route('/admin/tagdish_edit/save/<int:dish_id>', methods=['POST'])
@login_required
def admin_tagdish_save(dish_id):
    tags = Tag.select(Tag.tag_id,Tag.name, (~TagDish.TagDish_id.is_null().alias('check'))).join(TagDish,JOIN.LEFT_OUTER, on=((TagDish.tag_id==Tag.tag_id) & (TagDish.dish_id==dish_id)))
    if tags:
        for tag in tags:
            i=request.form.get(tag.name)
            if i=='1':
                j=TagDish.get_or_none((TagDish.dish_id==dish_id)&(TagDish.tag_id==tag.tag_id))
                if j is None:
                    TagDish.create(dish_id=dish_id,tag_id=tag.tag_id)
            else:
                query = TagDish.delete().where((TagDish.dish_id == dish_id) & (TagDish.tag_id == tag.tag_id))
                query.execute()
    return redirect(url_for('admin_dishes'))