# 消息提示

第一步：需要引入flash方法。
```
from flask import flash
```

第二步：在路由中定义消息提示
```
@app.route('/')
def index():
    flash('Welcome')
    return render_template('index.html')
```

第三步：在模板中获取消息提示内容。
```
{{ get_flashed_messages()[0] }}
```



#### 登录页面的交互案例：
```
# 路由
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

# 模板的主体内容：
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


# 异常

#### 抛出异常
引入并调用abort()方法可以手动抛出异常。
```
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
@app.errorhandler(404)
def notFound(e):
    return render_template('not_found.html')
```