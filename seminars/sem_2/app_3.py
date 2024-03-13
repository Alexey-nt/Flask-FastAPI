from flask import Flask, render_template, request

app = Flask(__name__)

LOGIN = 'admin'
PASSWORD = '1234'


@app.route('/', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    get_login = request.form.get('login')
    get_password = request.form.get('password')
    if get_login == LOGIN and get_password == PASSWORD:
        return render_template('successful.html')
    return render_template('error.html')


if __name__ == '__main__':
    app.run(debug=True)
