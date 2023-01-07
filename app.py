from flask import Flask, render_template

app = Flask(__name__)

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


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template("about.html", title="About")


@app.route('/login')
def login():
    return render_template('login.html', title='Login')


@app.route('/register')
def register():
    return render_template('register.html', title='Register')


if __name__ == '__main__':
    app.run()
