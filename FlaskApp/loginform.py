from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
import sqlite3


class LoginForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')
    conn = sqlite3.connect("One.db")
    cursor = conn.cursor()
    
    def log(self, username, password):
        self.username = username
        self.password = password
        cursor.execute("""CREATE  TABLE IF NOT All
                              (id INTEGER PRIMARY KEY AUTOINCREMENT,
                               email TEXT username,
                               password1 TEXT password
                               """)
