from flask import Flask, url_for, request, render_template

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


@app.route('/projects/')
def projects():
    return 'The project page'


@app.route('/about')
def about():
    return 'The about page'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        return 'Logando'
    else:
        return 'Login'


# with app.test_request_context():
#     """
#     /
#     /login
#     /login?next=/
#     /user/John%20Doe
#     """
#     print(url_for('index'))
#     print(url_for('login'))
#     print(url_for('login', next='/'))
#     print(url_for('profile', username='John Doe'))

@app.route('/template/')
@app.route('/template/erick')
def templates(name=None):
    return render_template('template.html', name=name)


if __name__ == '__main__':
    app.run(debug=True)
