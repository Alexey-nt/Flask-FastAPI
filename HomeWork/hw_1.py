from flask import Flask

app = Flask(__name__)

html = """
    <div header>
        <h1>Интернет-магазин</h1>
    </div>
    <div menu>
        <a href="#">Одежда</a>
        <a href="#">Обувь</a>
    </div>
    <div footter>
        <p>Контакты: г. Москва Ленина 50</p>
    </div>
"""


@app.route('/store/')
def store():
    return html


if __name__ == '__main__':
    app.run(debug=True)
