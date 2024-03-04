from flask import Flask, render_template

app = Flask(__name__)


@app.route('/about/')
def about_html():
    return 'about_html'


@app.route('/contacts/')
def contacts_html():
    return 'contacts_html'


@app.route('/number/<int:num1>/<int:num2>/')
def sum(num1, num2):
    return str(num1 + num2)


@app.route('/length/<text>/')
def text_length(text):
    return str(len(text))


html = """
<h1>Моя первая HTML страница</h1>
<p>Привет мир!</p>
"""


@app.route('/web/')
def web():
    return html


_users = [{'name': 'Ivan',
           'last_name': 'Ivanov',
           'age': '44',
           'average_mark': '4.8',
           },
          {'name': 'Ivana',
           'last_name': 'Ivanova',
           'age': '45',
           'average_mark': '4.3',
           }, ]


@app.route('/table/')
def table():
    return render_template('table.html', users=_users)


_news = [{'title': 'MAIN_news',
          'content': 'sdsdfsdgsdgsgsfgsfgsfg',
          'date': '2024-02-04',
          },
         {'title': 'other_news',
          'content': 'fgsfg',
          'date': '2024-02-05',
          }, ]


@app.route('/news/')
def news():
    return render_template('news.html', news=_news)


if __name__ == '__main__':
    app.run(debug=True)
