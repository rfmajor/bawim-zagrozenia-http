from flask import Blueprint
from flask import render_template, request, session, redirect, url_for

from app import get_db_connection

bp = Blueprint('login', __name__)


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']

        user = ''
        if session.get('logged_in'):
            user = session.get('username')

        connection = get_db_connection()
        with connection:
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM users WHERE username = ?;', (username,))
            account = cursor.fetchone()
            if account and account['password'] == password:
                session['logged_in'] = True
                session['id'] = account['id']
                session['username'] = account['username']
                return redirect(url_for('home.home', user=user))
            else:
                msg = 'Incorrect username / password !'
                return render_template('login.html', msg=msg, title="Sign In", user=user)
    else:
        return render_template('login.html')
