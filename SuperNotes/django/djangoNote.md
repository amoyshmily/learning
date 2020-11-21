# Django 学习笔记



## 一、入门热身



### 初入江湖

目标：创建后台页面



安装django库

`pip install django`



创建工程

`django-admin startproject student_sys`



创建应用

> student_sys\

`python manage.py startapp student`



编写models代码

> student_sys\student\models.py

```
from django.db import models


class Student(models.Model):
    SEX_ITEMS = [
        (1, '男'),
        (2, '女'),
        (0, '未知')
    ]

    STATUS_ITEMS = [
        (0, '申请'),
        (1, '通过'),
        (2, '拒绝')
    ]

    name = models.CharField(max_length=128, verbose_name='姓名')
    sex = models.ImageField(choices=SEX_ITEMS, verbose_name='性别')
    profession = models.CharField(max_length=128, verbose_name='职业')
    email = models.EmailField(verbose_name='Email')
    qq = models.CharField(max_length=128, verbose_name='QQ')
    phone = models.CharField(max_length=128, verbose_name='电话')
    status = models.IntegerField(choices=STATUS_ITEMS, default=0, verbose_name='审核状态')
    created_time = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='创建时间')

    def __str__(self):
        return '<Student: {}>'.format(self.name)

    class Meta:
        verbose_name = verbose_name_plural = '学员信息'

```

编写admin代码

> student_sys\student\admin.py

```
from django.contrib import admin

from .models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'sex', 'profession', 'email', 'qq', 'phone', 'status', 'created_time')

    list_filter = ('sex', 'status', 'created_time')
    search_fields = ('name', 'profession')
    fieldsets = (
        (None, {
            'fields': (
                'name',
                ('sex', 'profession'),
                ('email', 'qq', 'phone'),
                'status',
            )
        }),
    )


admin.site.register(Student, StudentAdmin)

```



注册student应用

> student_sys\student_sys\settings.py

```
INSTALLED_APPS = [
    'student',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```



迁移数据

`python manage.py makemigrations`

`python manage.py migrate`



创建超级管理员

`python manage.py createsuperuser`

amoy==sf.123456



启动服务

`python manage.py runserver`



在浏览器中访问：

`http://localhost:8000`即可访问项目。



后台管理地址：

`http://localhost:8000/admin`，输入超级管理员账号密码即可进入后台管理页面。



项目设置

> student_sys\student_sys\settings.py

```
LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True
```



编写视图函数

> student_sys\student\views

```
from django.shortcuts import render


def index(request):
    words = 'World!'
    return render(request, 'index.html', context={'words': words})

```



创建templates目录，新建index.html文件

> student\templates\index.html

```
<!DOCTYPE html>
<html>

    <head>
        <title>学员管理系统</title>
    </head>
    <body>
        Hello {{words}} ！
    </body>
</html>
```



修改路由

> student_sys\urls.py

```
from django.conf.urls import url
from django.contrib import admin

from student.views import index

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='index')
]
```



重新启动server后，访问`http://localhost:8000/`后页面将显示“Hello World ！”



---

### 小试牛刀

目标：创建前端表单页面



新建forms文件

> student\forms.py

普通青年

```
from django import forms

from .models import Student


class StudentForm(forms.Form):
    name = forms.CharField(label='姓名', max_length=128)
    sex = forms.ChoiceField(label='性别', choices=Student.SEX_ITEMS)
    profession = forms.CharField(label='职业', max_length=128)
    email = forms.EmailField(label='邮箱', max_length=128)
    qq = forms.CharField(label='QQ', max_length=128)
    phone = forms.CharField(label='手机', max_length=128)

```

文艺青年

```
from django import forms

from .models import Student


class StudentForm(forms.ModelForm):
    # 定义表单的字段
    class Meta:
        model = Student
        fields = (
            'name', 'sex', 'profession', 'email', 'qq', 'phone'
        )

    # 增加QQ号必须是纯数字的校验
    def clean_qq(self):
        cleaned_data = self.cleaned_data['qq']
        if not cleaned_data.isdigit():
            raise forms.ValidationError('QQ号必须是数字！')

```





修改模板

> student\templates\index.html

```
<!DOCTYPE html>
<html>

    <head>
        <title>学员管理系统</title>
    </head>
    <body>
        <h3><a href="/admin/">Admin</a></h3>
        <ul>
            {% for student in students %}
            <li>{{student.name}} - {{student.get_status_display}}</li>
            {% endfor %}
        </ul>
        <hr/>
        <form action="/" method="post">
            {% csrf_token %}
            {{ form }}
            <input type="submit" value="Submit">
        </form>
    </body>
</html>
```



优化模型

> student\models.py

```
# 增加一个类方法
@classmethod
    def get_all(cls):
        return cls.objects.all()
```





修改视图

> student\views.py

```
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Student
from .forms import StudentForm


def index(request):
    students = Student.get_all()

    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = StudentForm()

    context = {
        'students': students,
        'form': form,
    }

    return render(request, 'index.html', context=context)

```



---



### 视图类

> （原）视图函数 function view
>
> student\views.py

```
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Student
from .forms import StudentForm


def index(request):
    students = Student.get_all()

    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = StudentForm()

    context = {
        'students': students,
        'form': form,
    }

    return render(request, 'index.html', context=context)

```



> 视图类 class-based view
>
> student\views.py

```
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View

from .models import Student
from .forms import StudentForm



class IndexView(View):
    template_name = 'index.html'

    @staticmethod
    def get_context():
        students = Student.get_all()
        context = {'students': students}

        return context

    # 处理GET请求
    def get(self, request):
        context = self.get_context()
        form = StudentForm
        context.update({'form': form})

        return render(request, self.template_name, context=context)

    # 处理POST请求
    def post(self, request):
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
        context = self.get_context()
        context.update({'form': form})

        return render(request, self.template_name, context=context)

```

对应路由修改：

```
from django.conf.urls import url
from django.contrib import admin

from student.views import IndexView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^admin/', admin.site.urls)
]
```





### 中间件

middleware

student\middleware.py

```
import time

from django.utils.deprecation import MiddlewareMixin


class TimeItMiddleware(MiddlewareMixin):

    def process_request(self, request):
        self.start_time = time.time()
        return

    def process_view(self, request, func, *args, **kwargs):
        if request.path != reversed('index'):
            return

        start = time.time()
        response = func(request)
        cost = time.time() - start
        print('process view: {:.2f}s'.format(cost))
        return response

    def process_exception(self, request, exception):
        pass

    def process_template_response(self, request, response):
        return response

    def process_response(self, request, response):
        cost = time.time() - self.start_time
        print('request to response cost: {:.2f}s'.format(cost))
        return response


```





修改项目配置

student_sys\settings.py

```
MIDDLEWARE = [
    'student.middleware.TimeItMiddleware',
    
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```







## 二、博客实战



### 2.1 创建目录

```
typeidea
    │  CHANGELOG.md
    │  LICENCE
    │  README.md
    │  requirements.txt
    │
    ├─docs
    │      api文档.txt
    │      需求文档.txt
    │
    └─typeidea
        │  db.sqlite3
        │  manage.py
        │
        └─typeidea
                settings.py
                urls.py
                wsgi.py
                __init__.py
```



### 2.2 拆分配置

不同的配置分别定义成不同的模块。

操作：在`typeidea\typeidea`新建一个包，命名为settings。将原来的settings.py文件移入，并重命名为base.py



更新

> typeidea\typeidea\settings\base.py

```
LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'
```



> typeidea\typeidea\settings\develop.py

```
from .base import * # NOQA

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```

修改 manage.py和wsgi.py

> 更改前：os.environ.setdefault("DJANGO_SETTINGS_MODULE", "typeidea.settings")
>
> 更改后：
>
> ```
> profile = os.environ.get('TYPEIDEA_PROFILE', 'develop')
> os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'typeidea.settings.%s' % profile)
> ```

通过读取系统环境变量中的TPYEIDEA_PROFILE来控制Django加载不同的settings文件，从而达到开发环境使用develop.py，生产上使用product.py配置的目的。



> typeidea\manage.py


```
#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    # os.environ.setdefault("DJANGO_SETTINGS_MODULE", "typeidea.settings")
    profile = os.environ.get('TYPEIDEA_PROFILE', 'develop')
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'typeidea.settings.%s' % profile)
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    execute_from_command_line(sys.argv)

```



> typeidea\typeidea\wsgi.py

```
import os

from django.core.wsgi import get_wsgi_application

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "typeidea.settings")
profile = os.environ.get('TYPEIDEA_PROFILE', 'develop')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'typeidea.settings.%s' % profile)

application = get_wsgi_application()

```



### 2.3 编写Model

UML

E-R图

思维导图

#### 表设计

Category

Tag

Post

Comment

SIdebar

User

Link



 

#### 划分app

这里将Model划分为3类，好处是便于独立维护各个模块，也便于在开发时分配任务。

- blog相关（Category+Tag+Post）
- 配置相关
- 评论相关



#### 创建app



> Blog App

`python manage.py startapp blog`



> typeidea\blog\models.py

```
from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Category(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
    )

    name = models.CharField(max_length=50, verbose_name='名称')
    status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name='状态')
    is_nav = models.BooleanField(default=False, verbose_name='是否为导航')
    owner = models.ForeignKey(User, verbose_name='作者')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = verbose_name_plural = '分类'


class Tag(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
    )

    name = models.CharField(max_length=50, verbose_name='名称')
    status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name='状态')
    owner = models.ForeignKey(User, verbose_name='作者')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = verbose_name_plural = '标签'


class Post(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_DRAFT = 2
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
        (STATUS_DRAFT, '草稿'),
    )

    title = models.CharField(max_length=255, verbose_name='标题')
    desc = models.CharField(max_length=1024, blank=True, verbose_name='摘要')
    content = models.TextField(verbose_name='', help_text='正文必须是MarkDown格式')
    status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name='状态')
    category = models.ForeignKey(Category, verbose_name='分类')
    tag = models.ManyToManyField(Tag, verbose_name='标签')
    owner = models.ForeignKey(User, verbose_name='作者')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = verbose_name_plural = '文章'
        ordering = ['-id']  # 根据id进行降序排列

```



> Config App



```
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Link(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
    )

    title = models.CharField(max_length=50, verbose_name='标题')
    href = models.URLField(verbose_name='链接')   # 默认长度200
    status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name='状态')
    weight = models.PositiveIntegerField(default=1, choices=zip(range(1, 6), range(1, 6)), verbose_name='权重',
                                         help_text='权重高展示顺序靠前')
    owner = models.ForeignKey(User, verbose_name='作者')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = verbose_name_plural = '友链'


class Sidebar(models.Model):
    STATUS_SHOW = 1
    STATUS_HIDE = 0
    STATUS_ITEMS = (
        (STATUS_SHOW, '展示'),
        (STATUS_HIDE, '隐藏'),
    )
    SIDE_TYPE = (
        (1, 'HTML'),
        (2, '最新文章'),
        (3, '最热文章'),
        (4, '最近评论'),
    )

    title = models.CharField(max_length=50, verbose_name='标题')
    display_type = models.PositiveIntegerField(default=1, choices=SIDE_TYPE, verbose_name='展示类型')
    content = models.CharField(max_length=500, blank=True, verbose_name='内容',
                               help_text='如果设置的不是HTML类型，可为空')
    status = models.PositiveIntegerField(default=STATUS_SHOW, choices=STATUS_ITEMS, verbose_name='状态')
    owner = models.ForeignKey(User, verbose_name='作者')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = verbose_name_plural = '侧边栏'

```



> Comment App

```
from django.db import models

from typeidea.blog.models import Post


class Comment(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
    )

    target = models.ForeignKey(Post, verbose_name='评论目标')
    content = models.CharField(max_length=2000, verbose_name='内容')
    nickname = models.CharField(max_length=50, verbose_name='昵称')
    website = models.URLField(verbose_name='网站')
    email = models.EmailField(verbose_name='邮箱')
    status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name='状态')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = verbose_name_plural = '评论'

```

？？？？疑问：from typeidea.blog.models import Post这句问题

这样在makemigrations时报错。当改成from blog.models import Post则可以makemigrations但是models代码报错。





注册app



> typeidea\typeidea\settings\base.py

更新代码。注意app列表的先后顺序。

```
INSTALLED_APPS = [
    'blog',
    'config',
    'comment',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```



#### 建表

Django默认内置的是SQLite3数据库。如果需要使用MySQL等其他数据库，可以进行相应的配置（具体使用方法，后续会详细说明）。

在cmd中执行指令：`python manage.py makemigrations`

```
控制台输出：

Migrations for 'blog':
  blog\migrations\0001_initial.py
    - Create model Category
    - Create model Post
    - Create model Tag
    - Add field tag to post
Migrations for 'comment':
  comment\migrations\0001_initial.py
    - Create model Comment
Migrations for 'config':
  config\migrations\0001_initial.py
    - Create model Link
    - Create model Sidebar

```



在cmd中执行指令：`python manage.py migrate`

```
Operations to perform:
  Apply all migrations: admin, auth, blog, comment, config, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying blog.0001_initial... OK
  Applying comment.0001_initial... OK
  Applying config.0001_initial... OK
  Applying sessions.0001_initial... OK

```

如果需要查看数据库，可以使用`python manage.py dbshell`指令进入SQLite3数据库的交互界面。





#### ORM知识

Object Relational Mapping对象关系映射



##### 常用字段

1、数值型

| Django字段类         | 表字段类型 | 说明                                     |
| -------------------- | ---------- | ---------------------------------------- |
| AutoField            | int(11)    | 自增主键。                               |
| BooleanField         | tinyint(1) | 布尔类型，一般用于记录状态标记。         |
| DecimalField         | decimal    | 适用于需要高精度的场景，如支付金融相关。 |
| IntegerField         | int(11)    | 类似AutoField，但是不自增                |
| PositiveIntegerField | int(11)    | 类似IntegerField，只包含正整数           |
| SmallIntegerField    | smallint   | 小整数                                   |



2、字符型

除TextField是longtext类型外，其他均属于varchar类型。

| Django字段类型 | 表字段类型 | 说明                                                         |
| -------------- | ---------- | ------------------------------------------------------------ |
| charField      | varchar    | 基础的varchar类型                                            |
| URLField       | varchar    | 继承自CharField，实现了对URL的特殊处理                       |
| UUIDField      | char(32)   | 除PostgreSQL外，是固定长度，用来生成唯一id                   |
| EmailField     | varchar    | 继承自CharField，实现了对Email的特殊处理                     |
| FileField      | varchar    | 继承自CharField，实现了对文件的特殊处理，在admin部分展示时会自动生成一个上传文件的按钮。 |
| TextField      | longtext   | 一般用来存放大量文本内容，比如新闻正文、博客正文。           |
| ImageField     | varchar    | 继承自FileField，用来处理图片相关的数据                      |



3、日期类型

- DateField
- TimeField
- DateTimeField

4、关系类型

- ForeignKey
- OneToOneField
- ManyToManyField

其中外键和一对一其实是一种，只是一对一在外键的字段上加了unique。多对多会创建一个中间表，来进行多对多的关联。





##### 常用参数

| 参数             | 说明                                                         |
| ---------------- | ------------------------------------------------------------ |
| null             | 用于设定在数据库层面是否允许为空。                           |
| blank            | 针对业务层面该值是否允许为空。                               |
| choices          | 配置后可以在admin页面上展示对应的下拉选项。                  |
| db_column        | 指定Model中的某个字段对应数据库中的哪个字段。                |
| db_index         | 索引配置。用于业务经常需要作为查询条件的字段。               |
| default          | 默认值                                                       |
| editable         | 是否可编辑，默认是True。当设成False后页面不会展示。          |
| error_messages   | 字典格式，用来定义校验失败时的异常提示。key的可选项为null、blank、invalid、invalid_choice、unique和unique_for_date |
| help_text        | 字段提示语，在页面对应字段下方将展示此提示。                 |
| primary_key      | 主键。一个Model只允许设置一个字段为主键。                    |
| unique           | 唯一约束。当需要配置唯一值时，设置成True。设置完成后无需设置db_index。 |
| unique_for_date  | 针对date日期的联合约束，业务层面。用来限制一段时间内指定字段不能重复。 |
| unique_for_month | 针对月份的联合约束。                                         |
| unique_for_year  | 针对年份的联合约束。                                         |
| verbose_name     | 字段对应展示的文案。                                         |
| validators       | 自定义的校验逻辑，同form类似。                               |



##### QuerySet

###### 常用接口

> 懒加载：
>
> QuerySet本质上是一个懒加载的对象，作用是帮我们更友好地同数据库打交道。



> 链式调用：
>
> 执行对象的一个方法后返回的结果还是该对象，这样可以继续执行对象的其他方法。



> N+1问题：
>
> 一般情况，由外键查询产生的N+1问题比较多，即一条查询请求返回N条数据，当我们操作数据时，又会产生额外的请求。所有的ORM框架都存在这样的问题。

典型示例

```
posts = Post.objects.all()
for post in posts:	# 产生数据库查询
    print(post.owner)	# 产生额外的数据库查询，owner是外键
```

解决对策

```
# 针对一对多的关系
posts = Post.objects.all().select_related('owner')
for post in posts:
    print(post.owner)
```

```
# 针对多对多的关系
posts = Post.objects.all().prefetch_related('tag')
for post in posts:	# 产生了两条查询语句，分别查询post和tag
    print(post.tag.all())
```





- 支持链式调用的接口

| 接口     | 说明                                                         |
| -------- | ------------------------------------------------------------ |
| all      | 查询所有数据，相当于SELECT * FROM table_name...式的SQL       |
| filter   | 根据条件过滤数据。常用的条件是字段等于、不等于、大于、小于，还有类似like用法 |
| exclude  | 根据条件过滤数据，同filter逻辑相反                           |
| reverse  | 把QuerySet的结果倒序排列                                     |
| distinct | 对查询结果去重，相当于SELECT DISTINCE ...式的SQL             |
| none     | 返回空的QuerySet                                             |

- 不支持链式调用的接口

| 接口          | 说明                                                         |
| ------------- | ------------------------------------------------------------ |
| get           | 进行条件查询。如果查不到结果，则直接返回对象实例；如果不存在，则抛出DoesNotExist异常。 |
| create        | 用来直接创建一个Model对象。示例：post = Post.objects.create('title'='hello') |
| get_or_create | 根据条件查找，如果没有查到则调用create接口                   |
| bulk_create   | 批量创建记录，同create                                       |
| count         | 统计返回的QuerySet有多少条记录。相当于SELECT COUNT(&) FROM table_name语句 |
| latest        | 返回最新的一条记录，需要在Model中的Meta中定义 get_latest_by = 用来排序的字段 |
| earliest      | 返回最早的一条记录，需要在Model中的Meta中定义 get_earliest_by = 用来排序的字段 |
| first         | 返回当前QuerySet记录中的第一条                               |
| last          | 返回当前QuerySet记录中的最后一条                             |
| exists        | 判断QuerySet是否有数据，返回True或者False。                  |
| in_bulk       | 批量查询，接收2个参数id_list和field_name，返回结果是字典。键是查询条件，值是实例对象。 |
| update        | 根据条件批量更新记录。会触发Django的signal。                 |
| delete        | 根据条件批量删除记录。会触发Django的signal。                 |
| values        | 当明确知道只需要返回某个字段的值而不需要Model实例时使用。例如titles = Post.objects.filter(id=1).values('title')。返回的结果是包含字典的QuerySet，类似 QuerySet [{‘title’: 'hello'},] |
| values_list   | 类似values，直接返回的是包含元祖的QuerySet。例如QuerySet [('标题',)]。如果只是一个字段，则可以使用.value_list('title', flat=True) |



- 提高性能的接口

| 接口             | 说明                                                         |
| ---------------- | ------------------------------------------------------------ |
| defer            | 把不需要展示的字段做延迟加载，当需要的时候才会自动去加载。例如posts = Post.objects.all().defer('content')。当不想加载某个过大的字段时（如text类型的字段）会使用defer。 |
| only             | 与defer接口相反，只获取指定的字段                            |
| select_related   | 用来解决外键产生的N+1问题的方案，针对一对多的关联关系。      |
| prefetch_related | 用来解决外键产生的N+1问题的方案，针对多对多的关联关系。      |



###### 查询接口参数

| 字段        | 说明                                                         |
| ----------- | ------------------------------------------------------------ |
| contains    | 包含，用来进行相似查询，区分大小写。                         |
| icontains   | 同contains，忽略大小写。                                     |
| exact       | 精确匹配，区分大小写。                                       |
| iexact      | 同exact，忽略大小写。                                        |
| in          | 指定某个集合。                                               |
| gt          | 大于某个值，是greater than的缩写。                           |
| gte         | 大于等于某个值，是greater than or equal的缩写。              |
| lt          | 小于某个值，是less than的缩写。                              |
| lte         | 小于等于某个值，是less than or equal的缩写。                 |
| startswith  | 以某个字符串开头，等同于 LIKE '关键词 %'，区分大小写。       |
| istartswith | 同startswith，忽略大小写。                                   |
| endswith    | 以某个字符串结束，等同于 LIKE '关键词 %'，区分大小写。       |
| iendswith   | 同endswith，忽略大小写。                                     |
| range       | 范围查询，多用于时间范围。例如Post.objects.filter(created_time__range=('2020-11-11', '2020-12-12'))的效果是： SELECT ... WHERE created_time BETWEEN '2020-11-11' AND '2020-12-12'; |



###### 进阶查询

> F

F表达式用来执行数据库层面的计算，从而避免出现竞争状态。

问题背景：

```
post = Post.objects.get(id=1)
post.pv = post.pv + 1
post.save()
```

上述代码，在多线程执行的时候会有问题，每个线程的post.pv都是一样，执行完加1和保存后，相当于只执行了一次加1，而不是多次。原因是数据拿到python中转了一圈才被存到数据库中。

解决办法：

```
from django.db.models import F
    post = Post.objects.get(id=1)
    post.pv = F('pv') + 1
    post.save()
```

这种方式产生的SQL语句：'UPDATE blog_post SET pv = pv +1 WHERE id=1;'，它在数据库层面执行了原子性操作。



> Q

实现OR条件查询

```
from django.db.models import Q
posts = Post.objects.filter(Q(id=1) | Q(id=2))
```

实现AND条件查询

```
from django.db.models import Q
posts = Post.objects.filter(Q(id=1) & Q(id=2))
```



> Count

聚合查询

假设需要得到某个分类下有多少篇文章，按文章维度统计，可以写成：

```
category = Category.objects.get(id=1)
posts_count = category.post_set.count()
```

按分类的维度统计

```
from django.db.models import count
categories = Category.objects.annotate(posts_count = Count('post'))
print(categories[0].posts_count)
```

备注：QuerySet的annotate用来给QuerySet结果增加属性。这相当于给category动态增加了属性posts_count，而这个属性值来源于Count('post')。



> Sum

同Count类似，Sum是用来做合计。

例如，统计目前所有文章加起来的访问量有多多少，可以写成：

```
from django.db.models import Sum
Post.objects.aggregate(all_pv=Sum('pv'))
# 输出结果类似： {'all_pv': 487}
```

备注：QuerySet的aggregate用来直接计算结果。



> Avg
>
> Min
>
> Max



目前Model层所提供的接口完全是Django内置的，还没有进行自定义开发。

在操作数据库的便利性上，ORM提供了非常便利的接口，让我们不需要编写复杂的SQL语句就能够操作数据库。但同时需要意识到的是ORM的使用必定产生性能损耗。



###### 彩蛋

Django提供的原生SQL接口：raw。

它除了可以解决QuerySet无法满足的查询的情况外，还可以提高执行效率。

不过，我们要严格把控使用场景，因为过多地使用原生SQL会提高维护成本。

示例：

```
Post.objects.raw('SELECT * FROM blog_post')
```









### 2.4 开发管理后台

admin是Django的杀手锏。对于内容管理系统来说，当你有了数据库表，有了Model，就相当于自动拥有了一套管理后台，还包括权限验证。

Django是一个重Model的框架。当Model定义好了字段类型，上层可以根据这些字段类型定义form中需要呈现以及编辑的字段类型，这样就形成了表单。有了表单之后，基本上就有了增删改的页面。而基于QuerySet这个数据集合一级它所提供的查询操作，就有了列表的数据以及列表页的操作。



配置admin页面



### 2.5 开发前端界面







### 2.6 Bootstrap





## 三、第三方插件





### 四、API







## 五、上线

