from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    username = StringField('id ast', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    username_cap = StringField('Логин', validators=[DataRequired()])
    password_cap = PasswordField('Пароль', validators=[DataRequired()])
    submit = SubmitField('Доступ')