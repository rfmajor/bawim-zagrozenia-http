from flask import Blueprint
from flask import render_template, request, session

from app import get_db_connection

bp = Blueprint('login', __name__)


@bp.route('/login', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']

        connection = get_db_connection()
        with connection:
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM users WHERE username = ?;', (username,))
            account = cursor.fetchone()
            if account and account['password'] == password:
                session['loggedin'] = True
                session['id'] = account['id']
                session['username'] = account['username']
                msg = 'Logged in successfully !'
            else:
                msg = 'Incorrect username / password !'

    user = ''
    if session.get('loggedin'):
        user = session.get('username')
    return render_template('login.html', msg=msg, title="Sign In", user=user)
