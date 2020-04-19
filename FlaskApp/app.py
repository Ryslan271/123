import os
import sqlite3

from flask import Flask, render_template, request, redirect, flash, url_for
from flask_login import login_user, login_required
from forms import loginform

conn = sqlite3.connect("One.db")
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS employees(id INTEGER PRIMARY KEY AUTOINCREMENT,
 login1 TEXT, 
 password1 INTEGER)""")
conn.commit()
conn.close()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route("/")
def home():
    return render_template('Osnova.html')


@app.route("/Lyshee")
@login_required
def lyshee():
    return render_template('Lyshee.html')


@app.route("/O nas")
@login_required
def onas():
    return render_template('O nas.html')


@app.route("/Contact")
@login_required
def contact():
    return render_template('Contact.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = loginform.LoginForm()
  
    if form.validate_on_submit():
        return redirect('/login')

    return render_template('login.html', title='Авторизация', form=form)


@app.route('/regist', methods=['GET', 'POST'])
def register():
    global conn, cursor
    login_log = request.form.get('login')
    password = request.form.get('password')
    password2 = request.form.get('password2')

    if request.method == 'POST':
        if not (login_log or password or password2):
            flash('пожалуйста заполните все поля')
        elif password != password2:
            flash('пароли не совпадают')
        else:
            conn = sqlite3.connect("One.db")
            cursor = conn.cursor()
            cursor.execute("""UPDATE employees
                            SET login1 = 'login_log', 
                            password1 = 'password'
                            """)
            conn.commit()
            conn.close()

    return render_template("Regist.html")


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
