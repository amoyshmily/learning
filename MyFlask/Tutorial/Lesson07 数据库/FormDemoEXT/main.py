"""
使用Flask-wtf插件优化
2019-8-10 17:17:18
cifer woods
"""

from flask import Flask, request, redirect, render_template, url_for
from wtforms import Form, StringField, PasswordField, SubmitField, validators
from db import *

app = Flask(__name__)


class LoginForm(Form):
    username = StringField("username", [validators.data_required()])
    password = PasswordField("password", [validators.data_required()])
    btn_submit = SubmitField("submit")


@app.route('/user', methods=['GET', 'POST'])
def login():
    my_form = LoginForm(request.form)
    if request.method == 'POST':
        if isExisted(my_form.username.data, my_form.password.data) and my_form.validate():
            return redirect('https://baidu.com')
        else:
            msg = 'Login failed!'
            return render_template('index.html', message=msg, my_form=my_form)
    return render_template('index.html', my_form=my_form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    my_form = LoginForm(request.form)
    if request.method == 'POST':
        addUser(my_form.username.data, my_form.password.data)
        print(type(my_form.username.data))
        return 'Register Success!'

    return render_template('index.html', my_form=my_form)


@app.errorhandler(404)
def notFound(e):
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(port=8888, debug=True)
