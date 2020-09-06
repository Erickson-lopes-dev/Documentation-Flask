from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Olá, Mundo'


@app.route('/hello')
def hello():
    return 'Hello'


@app.route('/user/<username>')
def show_user_profile(username):
    return f'Username: {username}'


@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'Post {post_id}'


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return f'Subpath {subpath}'


if __name__ == '__main__':
    app.run(debug=True)