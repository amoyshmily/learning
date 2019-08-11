# Flask应用

#### 基本构成
```
from flask import Flask

app = Flask(__name__)

@app.route('/')
def fn():
    return 'Hello World!'
    
if __name__ == '__main__':
    app.run()
```

#### 路由
（1）简单路由
```
@app.route('/')
def test():
    return 'Hello World!'
```
（2）设定请求方式
```
@app.route('/user', methods=['POST'])
def test():
    return '{"name": "Amoy"}'
```
（3）显式传参
在路由的路径中，使用<>来定义所要接收的参数字段。
```

@app.route('/user/<user_id>')
def getUserId(user_id):
    return 'hello user:' + user_id
```
（4）隐式传参
在路由中无需指定参数字段，自动接收用户在url中输入的QueryString。
格式如：？xx=xx&xx=xx。

前提：引入request对象。
```
from flask import request

@app.route('/queryUser')
def queryUser():
    user_id = request.args.get('user_id')
    return 'query user: ' + user_id
```

#### 反向路由
通过视图函数，获取url地址。

前提：引入request对象，url_for方法。
```
from flask import request, url_for

@app.route('/queryUserByUserId')
def queryUser():
    user_id = request.args.get('user_id')
    return 'query user: ' + user_id

# 反向路由
@app.route('/getUrl')
def getUrl():
    return 'target url is :'+url_for('queryUser')


>>> 访问 /getUrl后
target url is :/queryUserByUserId
```