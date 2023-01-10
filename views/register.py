import re

import bcrypt
from flask import Blueprint, session
from flask import render_template, request
from app import get_db_connection


bp = Blueprint('register', __name__)


@bp.route('/register', methods=['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        connection = get_db_connection()
        with connection:
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM users WHERE username = ?;', (username,))
            account = cursor.fetchone()
            if account:
                msg = 'Account already exists !'
            elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
                msg = 'Invalid email address !'
            elif not re.match(r'[A-Za-z0-9]+', username):
                msg = 'Username must contain only characters and numbers !'
            elif not username or not password or not email:
                msg = 'Please fill out the form !'
            else:
                pwd_salt = bcrypt.gensalt()
                pwd_hash = bcrypt.hashpw(password.encode('utf-8'), pwd_salt).decode('utf-8')
                sql = f"INSERT INTO users (username, password, email, role) VALUES ('{username}', '{pwd_hash}', '{email}', 'USER');"
                cursor.execute(sql)
                connection.commit()
                msg = 'You have successfully registered !'
    elif request.method == 'POST':
        msg = 'Please fill out the form !'

    user = ''
    if session.get('logged_in'):
        user = session.get('username')
    return render_template('register.html', msg=msg, title="Sign Up", user=user)
