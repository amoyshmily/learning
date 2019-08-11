
from flask import Flask, flash, render_template, request, abort

app = Flask('__name__')
app.secret_key = '123'


@app.route('/')
def index():
    flash('Welcome')
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def login():
    my_form = request.form
    username = my_form.get('username')
    password = my_form.get('password')

    if not username:
        flash('请输入用户名！')
        return render_template('index.html')
    if not password:
        flash('请输入密码！')
        return render_template('index.html')
    if username == 'Amoy' and password == '123456':
        flash('登录成功！')
        return render_template('index.html')
    else:
        flash('用户名或者密码错误，请重新输入！')
        return render_template('index.html')


# 异常处理
@app.errorhandler(404)
def notFound(e):
    return render_template('not_found.html')


@app.route('/login/<user_id>')
def login_id(user_id):
    if int(user_id) == 1:
        return render_template('index.html')
    else:
        abort(404)  # 抛出404异常


if __name__ == '__main__':
    app.run()
