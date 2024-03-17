from flask import Flask
from project.lection_3.models_02 import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)


@app.route('/')
def index():
    return 'Hi!'


if __name__ == '__main__':
    app.run(debug=True)
