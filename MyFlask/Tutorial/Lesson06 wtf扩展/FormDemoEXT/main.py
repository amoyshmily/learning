"""
使用Flask-wtf插件优化
2019-8-10 17:17:18
cifer woods
"""

from flask import Flask, request, redirect, render_template
from wtforms import Form, StringField, PasswordField, SubmitField, validators

app = Flask(__name__)


class LoginForm(Form):
    # 使用wtf扩展
    username = StringField("username", [validators.data_required()])
    password = PasswordField("password", [validators.data_required()])
    btn_submit = SubmitField("submit")


@app.route('/user', methods=['GET', 'POST'])
def login():
    my_form = LoginForm(request.form)
    if request.method == 'POST':

        if my_form.username.data == 'cifer' and my_form.password.data == '123456' and my_form.validate():
            return redirect('https://baidu.com')
        else:
            msg = 'Login failed!'
            return render_template('index.html', message=msg, my_form=my_form)
    return render_template('index.html', my_form=my_form)


if __name__ == '__main__':
    app.run(port=8888)
