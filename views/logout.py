from flask import Blueprint, redirect, url_for
from flask import session

bp = Blueprint('logout', __name__)


@bp.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('id', None)
    session.pop('username', None)
    session.pop('user_role', None)
    return redirect(url_for('home.home'))
