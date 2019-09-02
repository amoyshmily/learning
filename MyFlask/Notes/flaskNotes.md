# Flask应用

## 基本构成
```
from flask import Flask

app = Flask(__name__)

@app.route('/')
def fn():
    return 'Hello World!'
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8888')    # 如果本地调试，则把host设置为‘127.0.0.1’。
```

## 路由

#### 简单路由
```
@app.route('/')
def test():
    return 'Hello World!'
```
#### 设定请求方式
```
@app.route('/user', methods=['POST'])
def test():
    return '{"name": "Amoy"}'
```
#### 显式传参
在路由的路径中，使用<>来定义所要接收的参数字段。
```

@app.route('/user/<int:user_id>')
def getUserId(user_id):
    return 'hello user:' + user_id
```
#### 隐式传参
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
（1）返回该视图函数的url地址。

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

（2）返回静态资源的地址
```
<link rel="shortcut icon" href="{{ url_for('static',filename='base/images/logo.png') }}">
```

#### 重定向
```
@app.route('/logout')
def logout():
    redirect(url_for('app.login'))
```


## 模板

#### 模板渲染

```
@app.route('/one')
def base():
    return render_template('index.html')
```

#### 模板传参
1.传递参数(给前端)
```
@app.route('/two')
def two():
    my_content = 'This is my content'
    return render_template('index.html', re_content=my_content)
    
在模板html引用示例：
<h3>{{re_content}}</h3>
```

2.传递对象
```
@app.route('/user')
def queryUser():
    my_user = User(user_id=1, user_name='Amoy')
    return render_template('user_index.html', re_user=my_user)

在模板html中引用示例： 
<h1>Hello {{re_user.user_name}}</h1>
```

#### 模板分支

```
# 后端代码
@app.route('/user/<int:user_id>')
def three(user_id):   
    my_user = User(user_id=1, user_name='Amoy') if user_id == 1 else None
    return render_template('user_id.html', re_user=my_user)

# 前端代码
<body>
    {% if re_user %}
        hello {{re_user.user_name}}
    {% else %}
        user not found!
    {% endif %}
</body>

```

#### 模板循环
```
# 后端代码
@app.route('/users')
def four():
    my_users = []
    for i in range(1, 11):
        user = User(user_id=i, user_name='Amoy' + str(i))
        my_users.append(user)

    return render_template('users_index.html', re_users=my_users)

# 前端代码
<body>
    {% for user in re_users %}
        {{user.user_id}} : {{user.user_name}} <br>
    {% endfor %}
</body>

```

#### 模板继承
```
# 前端代码
{% extends "base.html" %}
```

## 消息提示 flash

```
# 后端代码
from flask import flash

@app.route('/')
def index():
    flash('Welcome')
    return render_template('index.html')

# 前端代码
{{ get_flashed_messages()[0] }}
```



#### 消息交互案例：
```
# 后端代码
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

# 前端代码
<body>
    <h1>Welcome to login!</h1>

    <form action="/login" method="post">
        <input type="text" name="username">
        <input type="password" name="password">
        <input type="submit" value="submit">
    </form>

    <h2>{{ get_flashed_messages()[0] }}</h2>
</body>
```


## 异常处理

#### 抛出异常
```
# 后端代码
from flask import abort

@app.route('/login/<user_id>')
def login_id(user_id):
    if int(user_id) == 1:
        return render_template('index.html')
    else:
        abort(404)  # 抛出404异常
```


#### 处理异常
```
# 后端代码
@app.errorhandler(404)
def notFound(e):
    return render_template('not_found.html')
```

# 表单开发


#### 表单介绍
表单是HTML页面中负责数据采集功能的部件。
组成：表单标签、表单域、表单按钮。

表单标签：用于声明表单的范围，位于表单标签中的元素将被提交。
语法：<form></form>
属性：method,enctype,action

表单域
包含了文本框、密码框等多种类型
语法：<input />
属性：type,name,value
种类：
- 文本框 type=text
- 密码框 type=password
- 文本域 type=textarea
- 文件上传框 type=file
- 单选框 type=radio
- 复选框 type=checkbox

表单按钮
- 提交按钮
- 复位按钮
- 一般按钮

```
# html

<body>
    <form name="form1" action="">

        <input type="text" placeholder="text" name="text1">
        <input type="password" placeholder="password" name="password"><br />

        <textarea placeholder="textarea" name="textarea" id="" cols="30" rows="10"></textarea><br />

        <input type="file" name="file"><br />

        <input type="radio" name="radioInp" value="option1" />option1
        <input type="radio" name="radioInp" value="option2" />option2
        <input type="checkbox" name="checkboxInp" value="option1" />option1
        <input type="checkbox" name="checkboxInp" value="option2" />option2<br/>

        <input type="submit" value="submit">
        <input type="reset" value="reset">
        <input type="button" value="button" onclick="getValue()">

    </form>

</body>

# js
function getValue(){
    var text = document.form1.text1.value;
    alert(text)

    var text2 = document.form1.radioInp.value;
    alert(text2)

    var arr = document.form1.checkboxInp
    alert(arr[0].value)
}

```

## flask-wtf扩展

```
# 常规前端代码：
<form action="" name="form" method="post">
    Username: <input type="text" name="username" placeholder="username" />
    Password: <input type="password" name="password" placeholder="password" />
    <input type="submit" value="submit" />
</form>

# 使用wtf扩展的前端代码：
<form action="" name="form" method="post">
    Username: {{re_form.username}}<br/>
    Password: {{re_form.password}}<br/>
    {{re_form.btn_submit}}
</form>

# 后端代码
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
            return redirect(urlfor('app.index'))
        else:
            msg = 'Login failed!'
            return render_template('index.html', re_form=my_form)
    return render_template('index.html', re_form=my_form)
```