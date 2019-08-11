"""
Flask模板

（1）模板的简单使用
（2）条件语句
（3）循环语句
（4）模板的继承
"""

from flask import Flask, render_template
from MyFlask.Tutorial.Lesson02.Model import User

app = Flask(__name__)


# 没有使用模板
@app.route('/')
def base1():
    return 'Hello world!'


# 使用模板渲染
@app.route('/one')
def base():
    return render_template('index.html')


# 传参+模板渲染
@app.route('/two')
def two():
    my_content = 'This is my content'
    return render_template('index.html', content=my_content)


# 传递对象+模板渲染
@app.route('/user')
def queryUser():
    my_user = User(user_id=1, user_name='Amoy')
    return render_template('user_index.html', user=my_user)


# 模板分支
@app.route('/user/<user_id>')
def three(user_id):

    my_user = None

    if int(user_id) == 1:
        my_user = User(user_id=1, user_name='Amoy')

    return render_template('user_id.html', user=my_user)


# 模板循环
@app.route('/users')
def four():
    my_users = []
    for i in range(1, 11):
        user = User(user_id=i, user_name='Amoy'+str(i))
        my_users.append(user)

    return render_template('users_index.html', users=my_users)


# 模板继承
@app.route('/page_one')
def pageOne():
    return render_template('base_child_one.html')


@app.route('/page_two')
def pageTwo():
    return render_template('base_child_two.html')


if __name__ == '__main__':
    app.run()

