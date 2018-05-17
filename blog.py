from flask import Flask, render_template, request, session
from flask import flash, redirect, url_for, g

import sqlite3
# import os

#
# Configuration Section
#
DB_PATH = 'C:/Users/Justin/PythonProjects/flask-blog-database/blog.db'
USERNAME = 'admin'
PASSWORD = 'admin'
SECRET_KEY = 'hard_to_guess'

app = Flask(__name__)
app.config.from_object(__name__)


def connect_db():
    return sqlite3.connect(app.config['DB_PATH'])


@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    status_code = 200

    if request.method == 'POST':
        if request.form['username'] == app.config['USERNAME']:
            if request.form['password'] == app.config['PASSWORD']:
                session['logged_in'] = True
                return redirect(url_for('main'))
            else:
                error = 'Invalid Credentials. Please try again.'
                status_code = 401
        else:
            error = 'Invalid Credentials. Please try again.'
            status_code = 401

    return render_template('login.html', error=error), status_code


@app.route('/main')
def main():
    return render_template('main.html')


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
