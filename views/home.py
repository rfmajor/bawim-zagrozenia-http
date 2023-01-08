from flask import Blueprint, render_template, session, redirect, url_for, request
from app import get_db_connection

bp = Blueprint('home', __name__)


def fetch_posts():
    posts = None
    connection = get_db_connection()
    with connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM posts;')
        posts = cursor.fetchall()
    if session.get('logged_in'):
        author_id = session['id']
        for post in posts:
            if post['author_id'] == author_id:
                post['author'] = 'You'
    return posts


def add_post(title, content):
    if session.get('username') and session.get('id'):
        if title and content:
            username = session.get('username')
            author_id = session.get('id')
            connection = get_db_connection()
            with connection:
                connection.execute("INSERT INTO posts(author_id, author, title, content) VALUES (?, ?, ?, ?)",
                                   (author_id, username, title, content))
    else:
        raise Exception('Not logged in')


def delete_post(post_id):
    if session.get('logged_in') and session.get('username') and session.get('id'):
        user_id = session.get('id')
        connection = get_db_connection()
        with connection:
            connection.execute("DELETE FROM posts WHERE id = ? AND author_id = ?", (post_id, user_id))
    else:
        raise Exception('Failed to delete row')


@bp.route('/')
@bp.route('/home', methods=['GET', 'POST'])
def home():
    user = ''
    if session.get('logged_in'):
        user = session.get('username')

    if request.method == 'POST' and 'post_content' in request.form and 'post_title' in request.form:
        add_post(request.form['post_title'], request.form['post_content'])
    return render_template('home.html', posts=fetch_posts(), user=user)


@bp.route('/home/delete/<post_id>')
def delete(post_id):
    delete_post(post_id)
    return redirect(url_for('home.home'))