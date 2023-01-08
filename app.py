from flask import Flask
import sqlite3 as sl


def _db_init():
    with open('static/init.sql', 'r') as sql_file:
        sql_script = sql_file.read()

    connection = get_db_connection()

    cursor = connection.cursor()
    print('Executing init script: \n' + sql_script)
    cursor.executescript(sql_script)
    connection.commit()
    connection.close()


def _dict_factory(dict_cursor, row):
    d = {}
    for idx, col in enumerate(dict_cursor.description):
        d[col[0]] = row[idx]
    return d


def get_db_connection():
    connection = sl.connect('database.db')
    connection.row_factory = _dict_factory
    return connection


def create_app():
    app = Flask(__name__)

    app.secret_key = 'your secret key'

    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = 'root'
    app.config['MYSQL_DB'] = 'mywebsite'

    _db_init()

    from views.home import bp as bp_home
    from views.about import bp as bp_about
    from views.login import bp as bp_login
    from views.logout import bp as bp_logout
    from views.register import bp as bp_register

    app.register_blueprint(bp_home)
    app.register_blueprint(bp_about)
    app.register_blueprint(bp_login)
    app.register_blueprint(bp_logout)
    app.register_blueprint(bp_register)

    return app


if __name__ == '__main__':
    create_app()
