from flask import Flask, url_for, request, render_template
import sqlite3
app = Flask(__name__)
conn = sqlite3.connect("One.db")
cursor = conn.cursor()
cursor.execute("""CREATE  TABLE IF NOT All
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       email TEXT NOT NULL,
                       password1 TEXT NOT NULL,
                       password2 TEXT NOT NULL)
                   """)


def astronaut_selection():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='static/css.css')}" />
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                            <h1 align="center">Анкета претендента</h1>
                            <h3 align="center">на участие в миссии</h3>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="text" class="form-control" id="surname" aria-describedby="surnamelHelp" placeholder="Введите имя" name="surname">
                                    <br>
                                    <input type="text" class="form-control" id="name" aria-describedby="nameHelp" placeholder="Пароль" name="password1">
                                    <br>
                                    <input type="text" class="form-control" id="name" aria-describedby="nameHelp" placeholder="Повторите пароль" name="password2">
                                    <br>
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="маил" name="email">
                                    <div class="form-group">
                                        <label for="eduSelect">Какое у Вас образование?</label>
                                        <select class="form-control" id="classSelect" name="edu">
                                          <option>Начальное</option>
                                          <option>Среднее</option>
                                          <option>Выше среднего</option>
                                          <option>Супер!</option>
                                        </select>
                                    <br>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    cursor.execute("""UPDATE All
                          SET request.form['email'] WHERE email,
                          SET request.form['password1'] WHERE password1,
                          SET request.form['password2'] WHERE password2
                       """)

    return render_template('Osnova.html')