"""
Задание №4
Создать страницу, на которой будет форма для ввода текста и
кнопка "Отправить"
При нажатии кнопки будет произведен подсчет количества слов
в тексте и переход на страницу с результатом.

"""
from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/count/', methods=['POST'])
def count():
    text = request.form["text"]
    count = len(text.split())
    return render_template('count.html', count=count)



if __name__ == '__main__':
    app.run(debug=True)
