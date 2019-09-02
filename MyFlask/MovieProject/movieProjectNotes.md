


# 蓝图构建项目

#### 什么是蓝图
一个应用中或跨应用制作应用组件和支持通用的模式。


#### 蓝图的作用
- 将不同的功能模块化
- 构建大型应用
- 优化项目结构
- 增强可读性，易于维护

```
1.定义蓝图 app/admin/__init__.py
from flask import Blueprint
import views

admin = Blueprint("admin", __name__)

2.注册蓝图 app/__init__.py
from admin import admin as admin_blueprint

app.register_blueprint(admin_blueprint, url_prefix="/admin")

3.调用蓝图 app/admin/views.py
from . import admin

@admin.route('/')
```

# 数据库ORM

##### 1.安装模块
```
pip install flask-sqlalchemy
```

##### 2.建立连接
```
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://user:password@127.0.0.1/db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
```

##### 数据模型
```
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)    # 编号
    name = db.Column(db.String(100), unique=True)   # 昵称
    pwd = db.Column(db.String(100)) # 密码
    email = db.Column(db.String(100), unique=True)  # 邮箱
    phone = db.Column(db.String(11), unique=True)   # 手机号码
    info = db.Column(db.Text)   # 个人简介
    face = db.Column(db.String(255), unique=True)   # 头像
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)  # 注册时间
    uuid = db.Column(db.String(255), unique=True)   # 唯一标识符
    user_logs = db.relationship('UserLog', backref='user')  # 外键关系关联

    def __repr__(self):
        return '<User %r>' % self.name

```

