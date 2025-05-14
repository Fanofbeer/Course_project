from wtforms import IntegerField, validators
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired

class AddUserForm(FlaskForm):
    user_id = IntegerField('ID пользователя', [
        validators.InputRequired(),
        validators.NumberRange(min=1)
    ])
    username = StringField('Имя пользователя', [
        validators.InputRequired(),
        validators.Length(min=3, max=50)
    ])

class EditUserForm(FlaskForm):
    username = StringField('Имя пользователя', [
        validators.InputRequired(),
        validators.Length(min=3, max=50)
    ])

class LoginForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])