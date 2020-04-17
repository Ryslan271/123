from flask import render_template, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
import sqlite3 as lite
import sqlite3


class LoginForm(FlaskForm):
        def __init__(self, username, password, remember_me, submit):
        self.username = username
        self.password = password
        self.remember_me = remember_me
        self.submit = submit
        username = StringField('Логин', validators=[DataRequired()])
        password = PasswordField('Пароль', validators=[DataRequired()])
        remember_me = BooleanField('Запомнить меня')
        submit = SubmitField('Войти')
        
        self.log(self.username)

    def log(self, username):
        self.username = username
        conn = sqlite3.connect("One.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM All")
        rows = cursor.fetchall()

        for row in rows:
            if row == self.username:
                return render_template("Osnova.html")
            else:
                return render_template(url_for('register'))
