from flask import Flask, render_template
import os
import psycopg2

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


@app.route("/regist")
def regist():
    return render_template('regist.html')


@app.route("/regi")
def regi():
    con = psycopg2.connect(
        database="postgres",
        user="postgres",
        password="Qazwsxedc",
        host="127.0.0.1",
        port="5432"
    )
    cur = con.cursor()
    cur.execute('''CREATE TABLE STUDENT 
    (Mail TEXT PRIMARY KEY NOT NULL, 
    Power INT NOT NULL);''')
    con.commit()
    con.close()


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
