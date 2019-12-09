### HttpRunnerManager环境配置

1.安装MySQL数据库
创建HttpRunnerManager库
2.下载HttpRunnerManager项目
3.安装Erlang
下载地址：http://www.erlang.org/downloads

4.安装Rabbitmq
下载地址：http://www.rabbitmq.com/download.html

5.修改配置文件/HttpRunnerManager/settings.py
- 更新其中的数据库连接信息。
更改后：
```
if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'HttpRunnerManager',  # 新建数据库名
            'USER': 'root',  # 数据库登录名
            'PASSWORD': '123456',  # 数据库登录密码
            'HOST': '127.0.0.1',  # 数据库所在服务器ip地址
            'PORT': '3306',  # 监听端口 默认3306即可
        }
    }
    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, 'static'),  # 静态文件额外目录
    )
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'HttpRunnerManager',  # 新建数据库名
            'USER': 'root',  # 数据库登录名
            'PASSWORD': '123456',  # 数据库登录密码
            'HOST': '127.0.0.1',  # 数据库所在服务器ip地址
            'PORT': '3306',  # 监听端口 默认3306即可
        }
    }
```

- 修改BROKER_URL

更改后：
```
BROKER_URL = 'amqp://dev:zwc123@192.168.91.45:5672//' if DEBUG else 'amqp://dev:zwc123@192.168.91.45:5672//'
```

- 修改邮箱
更改后：
```
EMAIL_SEND_USERNAME = 'sincerely1314521@163.com'  # 定时任务报告发送邮箱，支持163,qq,sina,企业qq邮箱等，注意需要开通smtp服务
EMAIL_SEND_PASSWORD = 'TANGxinbing135!'     # 邮箱密码
```

6.安装依赖库
进入项目根目录，打开cmd，执行
```
pip install -r requirements.txt
```

7.数据库迁移
进入项目根目录，打开cmd，执行
```
python manage.py makemigrations ApiManager  # 生成迁移脚本
python manage.py migrate    # 应用到db生成数据表
```

8.创建后台超级管理员用户
进入项目根目录，打开cmd，执行
```
python manage.py createsuperuser
```

9.启动服务
```
python manage.py runserver
```

10.访问应用
http://127.0.0.1:8000/api/register/
进行注册和登录。






#### httprunner上传文件multipart/form-data
```
Rquest Payload
    ------WebKitFormBoundarymAyGmnyhpf3UBdec
    Content-Disposition: form-data; name="sysCode"

    S04
    ------WebKitFormBoundarymAyGmnyhpf3UBdec
    Content-Disposition: form-data; name="subSysCode"

    S0401
    ------WebKitFormBoundarymAyGmnyhpf3UBdec
    Content-Disposition: form-data; name="fileType"

    image
    ------WebKitFormBoundarymAyGmnyhpf3UBdec
    Content-Disposition: form-data; name="filePermission"

    PUBLIC
    ------WebKitFormBoundarymAyGmnyhpf3UBdec
    Content-Disposition: form-data; name="file"; filename="2.jpg"
    Content-Type: image/jpeg
    ------WebKitFormBoundarymAyGmnyhpf3UBdec--


#yaml用例
- test:
    name: 上传文件
    request:
        url: $url/api/add
        method: POST
        files:
            sysCode: [null,'S04']
            subSysCode: [null,'S0401']
            fileType: [null,'image' ]
            filePermission: [null,'PUBLIC']
            file: ['2.jpg',$file1,'image/jpeg']
    extract:
        - fileId: content.responseBody.fileId
    validate:
        - eq: [status_code, 200]
        - eq: [content.status, SUCCESS]
        - eq: [content.status, SUCCESS]
    variables:
        - filePath: "D:\\Pictures\\2.jpg"
        - file1: ${get_file($filePath)}


#debugtalk.py
# 读取文件内容
def get_file(filePath):
    return open(filePath, "rb")
```

#### 断言
```
validate两种格式

validate支持两种格式：

{"comparator_name": [check_item, expect_value]}
{"check": check_item, "comparator": comparator_name, "expect": expect_value}


validate:
        - check: status_code
          comparator: eq
          expect: 200
 
        - check: status_code
          comparator: less_than
          expect: 400
 
        - check: content.code
          comparator: equals
          expect: 0
 
        - check: content.msg
          comparator: equals
          expect: success!

```