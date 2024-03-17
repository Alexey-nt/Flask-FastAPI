from datetime import datetime, timedelta

from flask import Flask, render_template, jsonify, request
from project.lection_3.models_05 import db, User, Post
from flask_wtf import FlaskForm
from flask_wtf.csrf import CSRFProtect
from forms_1 import LoginForm, RegistrationForm

app = Flask(__name__)
app.config['SECRET_KEY'] =  'mysecretkey'
csrf = CSRFProtect(app)
"""
Генерация надёжного секретного ключа
>>> import secrets
>>> secrets.token_hex()
"""
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../../instance/mydatabase.db'
db.init_app(app)


@app.route('/')
def index():
    return 'Hi!'


@app.route('/form/', methods=['GET', 'POST'])
@csrf.exempt
def my_form():
    ...
    return 'No CSRF protection!'


@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate():
        # Обработка данных из формы
        pass
    return render_template('login.html', form=form)



@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        # Обработка данных из формы
        email = form.email.data
        password = form.password.data
        print(email, password)
    ...
    return render_template('register.html', form=form)



@app.route('/data/')
def data():
    return 'Your data!'


@app.route('/users/')
def all_users():
    users = User.query.all()
    context = {'users': users}
    return render_template('users.html', **context)


@app.route('/users/<username>/')
def users_by_username(username):
    users = User.query.filter(User.username == username).all()
    context = {'users': users}
    return render_template('users.html', **context)


@app.route('/posts/author/<int:user_id>/')
def get_posts_by_author(user_id):
    posts = Post.query.filter_by(author_id=user_id).all()
    if posts:
        return jsonify([{'id': post.id,
                         'title': post.title,
                         'content': post.content,
                         'created_at': post.created_at} for post in posts])
    else:
        return jsonify({'error': 'Posts not found'}), 404


@app.route('/posts/last-week/')
def get_posts_last_week():
    date = datetime.utcnow() - timedelta(days=7)
    posts = Post.query.filter(Post.created_at >= date).all()
    if posts:
        return jsonify([{'id': post.id,
                         'title': post.title,
                         'content': post.content,
                         'created_at': post.created_at} for post in posts])
    else:
        return jsonify({'error': 'Posts not found'})


if __name__ == '__main__':
    app.run(debug=True)
