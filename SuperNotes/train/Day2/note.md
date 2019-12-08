#### 安装Django框架
```
常规安装
pip install Django

或者使用豆瓣源安装
pip install Django -i http://pypi.douban.com/simple 
--trusted-host pypi.douban.com
```

#### 创建mysite项目
```
在项目根目录，打开cmd窗口，输入指令：
django-admin startproject mysite .
```

#### 运行mysite项目
```
在项目根目录，打开cmd窗口，输入指令：
python manage.py runserver

然后打开浏览器，访问localhost:8000，如果正常打开，则表明项目运行正常。
```

#### 创建blog应用
```
在项目根目录，打开cmd窗口，输入指令：
python manage.py startapp blog
```

#### 配置mysite项目
```
项目配置文件：mysite目录中的settings.py

（1）注册blog应用：
在【INSTALLED_APPS】列表中，添加元素 “'blog',”。
注意末尾的半角逗号不能省略。

（2）数据库配置
【DATABASES】节点，默认是sqlite数据库。

（3）声明语言
【LANGUAGE_CODE】节点
LANGUAGE_CODE = 'en-us' 表示使用英文
LANGUAGE_CODE = 'zh-hans' 表示使用中文

(4)配置时区
【TIME_ZONE】节点
TIME_ZONE = 'UTC' 使用格林尼治时间
TIME_ZONE = 'UTC' 使用东八区时间
```

