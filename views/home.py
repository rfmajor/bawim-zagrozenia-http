from flask import Blueprint, render_template, session
from app import get_db_connection

bp = Blueprint('home', __name__)


def fetch_posts():
    posts = None
    connection = get_db_connection()
    with connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM posts;')
        posts = cursor.fetchall()
    return posts


@bp.route('/')
@bp.route('/home')
def home():
    user = ''
    if session.get('loggedin'):
        user = session.get('username')

    return render_template('home.html', posts=fetch_posts(), user=user)
