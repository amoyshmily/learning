from flask import Flask, request, redirect, render_template

app = Flask(__name__)


@app.route('/user', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == 'cifer' and password == '123456':
            return redirect('https://baidu.com')
        else:
            msg = 'Login failed!'
            return render_template('index.html', message=msg)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(port=8888)
