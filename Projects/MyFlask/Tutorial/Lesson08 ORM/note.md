
# 留言板实战

#### 依赖包
```
# 安装
pip install flask-sqlalchemy

```

#### 使用方法

```

推荐保存独立文件：model.py

# 引用
from flask_sqlalchemy import SQLAlchemy
import pymysql
pymysql.install_as_MySQLdb()

# 实例化
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@127.0.0.1:3306/flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

# 插入数据
try:
    db.session.add(obj)
    db.session.commit()
except:
    db.session.rollback()
finally:
    doSomething()

# 查询数据
obj = Obj.query.filter_by(field1=self.XX, field2=self.XXX).first()

注意：因为在这个model.py模型文件中已经示例化了，db = SQLAlchemy(app)，所以在视图函数中
直接引用app = db.app即可，千万不要另行示例化出一个app = Flask(__name__),否则容易报错
“KeyError: 'SQLALCHEMY_TRACK_MODIFICATIONS'”。
```