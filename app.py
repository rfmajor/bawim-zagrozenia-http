from flask import Flask
from flask_mysqldb import MySQL

db = MySQL()


def create_app():
    app = Flask(__name__)

    app.secret_key = 'your secret key'

    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = 'root'
    app.config['MYSQL_DB'] = 'mywebsite'

    db.init_app(app)

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
