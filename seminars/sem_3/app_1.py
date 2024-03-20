"""
Задание №1
Создать базу данных для хранения информации о студентах университета.
База данных должна содержать две таблицы: "Студенты" и "Факультеты".
В таблице "Студенты" должны быть следующие поля: id, имя, фамилия,
возраст, пол, группа и id факультета.
В таблице "Факультеты" должны быть следующие поля: id и название
факультета.
Необходимо создать связь между таблицами "Студенты" и "Факультеты".
Написать функцию-обработчик, которая будет выводить список всех
студентов с указанием их факультета.
"""

from flask import Flask, render_template
from models import db, Students, Fags, Gender
from random import choice, randint

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app_1.db'
db.init_app(app)


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')


@app.cli.command("add-user")
def add_user():
    for _ in range(1, 11):
        fag = Fags(fag_name=choice(['math', 'history', 'languages']))
        db.session.add(fag)
    db.session.commit()

    for i in range(1, 11):
        student = Students(name=f'name{i}',
                           lastname=f'lastname{i}',
                           age=i + 15,
                           gender=choice([Gender.male, Gender.female]),
                           group=choice([1, 2, 3]),
                           fags_id=randint(1, 10))
        db.session.add(student)
    db.session.commit()
    print('Students add in DB!')


@app.route('/')
def index():
    student = Students.query.all()
    return render_template('index.html', student=student)

if __name__ == '__main__':
    app.run(debug=True)
