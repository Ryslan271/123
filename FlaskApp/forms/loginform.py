import sqlite3

from flask import render_template, url_for
from flask_sqlalchemy import itervalues
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    def __init__(self):
        username = StringField('Логин', validators=[DataRequired()])
        password = PasswordField('Пароль', validators=[DataRequired()])
        remember_me = BooleanField('Запомнить меня')
        submit = SubmitField('Войти')
        self.username = username
        self.password = password
        self.remember_me = remember_me
        self.submit = submit

    def login(self, username):
        self.username = username
        conn = sqlite3.connect("One.db")
        cursor = conn.cursor()
        cursor.execute('SELECT login1 FROM employees')
        rows = cursor.fetchall()

        for row in rows:
            if row == self.username:
                return render_template("Osnova.html")
            else:
                return render_template(url_for('register'))