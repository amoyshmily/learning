"""
Flask应用的基本构成
Flask的路由
Flask的反向路由
"""

from flask import Flask, request, url_for

app = Flask(__name__)


@app.route('/')
def helloWorld():
    return 'Hello World!'


# 设置请求方式
@app.route('/user', methods=['POST'])
def postApi():
    return 'Hello user!'


# 显式传参（占位）
@app.route('/users/<user_id>')
def getUserId(user_id):
    return 'hello user:' + user_id


# 隐式传参（QueryString方式：？xx=xx&xx=xx）
@app.route('/queryUser')
def queryUser():
    user_id = request.args.get('user_id')
    return 'query user: ' + user_id


# 反向路由：通过视图函数，获取url地址
@app.route('/queryUrl')
def queryUrl():
    return 'query url:'+url_for('queryUser')


if __name__ == '__main__':
    app.run()
