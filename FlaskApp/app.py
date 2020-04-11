from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
import os

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


@app.route('/regist')
def login():
    return render_template('Con1.py')


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
