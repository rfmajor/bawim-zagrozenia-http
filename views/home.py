from flask import Blueprint, render_template

bp = Blueprint('home', __name__)

posts = [
    {
        'author': 'Me',
        'title': 'first',
        'content': 'Lorem ipsum'
    },
    {
        'author': 'You',
        'title': 'second',
        'content': 'Lorem ipsum'
    }
]


@bp.route('/')
@bp.route('/home')
def home():
    return render_template('home.html', posts=posts)
