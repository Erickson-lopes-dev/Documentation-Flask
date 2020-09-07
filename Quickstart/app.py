from flask import Flask, url_for, request, render_template
from werkzeug.utils import secure_filename

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
    user, pwd = 'erick', 'admin'
    error = 'Usuário não encontrado'

    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        if str(username) == user and str(password) == pwd:
            print(username, password)
            return render_template('template.html', username=username, password=password)

        else:
            print(error)
            return render_template('login.html', error=error)

    else:
        return render_template('login.html')


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

# renderizando templates
@app.route('/template/')
@app.route('/template/erick')
def templates(name=None):
    return render_template('template.html', name=name)


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        f = request.files['image']
        f.save('/Imagens' + secure_filename(f.filename))
        return render_template('img.html', message='Imagem Salva')

    return render_template('img.html')


@app.route('/cookie')
def cookie():
    username = request.cookies.get('username')
    return render_template('cookie.html', user=username)


if __name__ == '__main__':
    app.run(debug=True)
