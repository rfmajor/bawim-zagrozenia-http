from flask import Blueprint, render_template, session

bp = Blueprint('about', __name__)


@bp.route('/about')
def about():
    if session.get('logged_in'):
        user = session.get('username')
        return render_template("about.html", title="About", user=user)
    else:
        return render_template("about.html", title="About")
