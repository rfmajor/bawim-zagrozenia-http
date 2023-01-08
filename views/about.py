from flask import Blueprint, render_template, session
from app import get_db_connection

bp = Blueprint('about', __name__)


def fetch_user_posts(author_id):
    posts = None
    connection = get_db_connection()
    with connection:
        cursor = connection.cursor()
        query = 'SELECT * FROM posts WHERE author_id='+str(author_id)+';'
        cursor.execute(query)
        posts = cursor.fetchall()
    return posts


@bp.route('/about')
def about():
    if session.get('logged_in'):
        user = session.get('username')
        posts = fetch_user_posts(session.get('id'))
        return render_template("about.html", title="About", user=user, posts=posts)
    else:
        return render_template("about.html", title="About")
