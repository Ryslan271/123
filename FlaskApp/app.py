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
    return render_template('1_5.py')


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
