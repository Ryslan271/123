import sqlite3

from flask import render_template, url_for
from flask_sqlalchemy import itervalues
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

f = None

conn = sqlite3.connect("One.db")
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS employees(id INTEGER PRIMARY KEY AUTOINCREMENT,
 login1 TEXT, 
 password1 INTEGER)""")
conn.commit()
conn.close()


def login():
    global f
    if f:
        return render_template('Osnova.html')
    else:
        return redirect('/regist')


class LoginForm(FlaskForm):
    global f
    username = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')
    conn = sqlite3.connect("One.db")
    cursor = conn.cursor()
    cursor.execute('SELECT login1 FROM employees')
    rows = cursor.fetchall()

    for row in rows:
        if row == username:
            f = True
        else:
            f = False
    login()
