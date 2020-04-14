from flask import Flask, render_template, request
import os
import sqlite3

conn = sqlite3.connect("One.db")
cursor = conn.cursor()

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('Osnova.html')


@app.route("/Lyshee")
def lyshee():
    return render_template('Lyshee.html')


@app.route("/O nas")
def onas():
    return render_template('O nas.html')


@app.route("/Contact")
def contact():
    return render_template('Contact.html')


@app.route('/regist', methods=['POST', 'GET'])
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
    
    cursor.execute("""CREATE TABLE All
                      (title text, artist text, release_date text,
                       publisher text, media_type text)
                   """)


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
