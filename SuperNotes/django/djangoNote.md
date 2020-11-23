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


class SideBar(models.Model):
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
    - Create model SideBar

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



创建超级管理员

`python manage.py createsuperuser`

cifer1024==sf.520198



#### 2.4.1 配置admin页面



**ModelAdmin**

通过继承admin.ModelAdmin，就能实现对这个Model的增、删、改、查页面的配置。这里的ModelAdmin是很重要的一环，后面还会接触到ModelForm概念，这些都是跟Model紧耦合的，在Model上可以实现更多业务逻辑。



##### 配置blog应用



> typeidea\blog\admin.py

```
from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import Category, Tag, Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'is_nav', 'post_count', 'created_time')  # 列表展示的字段
    fields = ('name', 'status', 'is_nav')  # 新增表单的条目

    # 重写ModelAdmin的save_model方法
    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(CategoryAdmin, self).save_model(request, obj, form, change)

    # 自定义函数：展示该分类有多少篇文章
    def post_count(self, obj):
        return obj.post_set.count()

    post_count.short_description = '文章数量'


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'created_time')  # 列表展示的字段
    fields = ('name', 'status')  # 新增表单的条目

    # 重写ModelAdmin的save_model方法
    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(TagAdmin, self).save_model(request, obj, form, change)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    # ------ 列表页面：结果列部分表
    # 搜索框（在结果列表顶部，列表中的字段是表示支持检索的字段）
    search_fields = ['title', 'category__name']
    
    # 查询结果列表展示
    list_display = ['title', 'category', 'status', 'owner', 'created_time', 'operator']
    list_display_links = []

	# 在结果列表末尾加入一列，列名叫“操作”
    def operator(self, obj):
        return format_html('<a href="{}">编辑</a>', reverse('admin:blog_post_change', args=(obj.id,)))
    operator.short_description = '操作'

    # 针对列表的操作（默认展示在列表上/下侧位置）
    actions_on_top = True
    actions_on_bottom = True

    # ------ 列表页面：过滤器
    # 页面过滤器（默认展示在右侧）
    list_filter = ['category']

    # ------ 新增编辑页面
    # 顶部是否展示保存按钮（默认是有一个在表单底部）
    save_on_top = True

    # 新增表单的内容
    fields = (
        ('title', 'category'),  # 嵌套元祖表示这几个字段在页面上处在同一排
        ('desc', 'status'),
        'content',
        'tag',
    )

    # 重写ModelAdmin的save_model方法
    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(PostAdmin, self).save_model(request, obj, form, change)

```

备注1：

​	重写ModelAdmin的save_model方法。这里的request就是当前请求，obj是当前要保存的对象，form是页面	提交过来的表单之后的对象，change用于标志本次保存的数据是新增的还是更新的。

备注2：

- list_display：用来配置列表页面展示哪些字段。

- list_display_links：用来配置哪些字段可以作为链接。点击它们，可以进入编辑页面。

- list_filter：配置页面过滤器，需要通过哪些字段来过滤列表页。

- search_fields：配置搜索字段。

- actions_on_top：动作相关的配置，是否展示在顶部。

- actions_on_bottom：动作相关的配置，是否展示在底部。

- save_on_top：控制保存、编辑、编辑并新建按钮是否在顶部展示。

  详细文档：https://docs.djangoproject.com/en/1.11/ref/contrib/admin/#modeladmin-opotions



细节优化

>  优化前：
>
> 当添加分类操作成功后，表头部分会提示文案：“分类 "[Category object](http://localhost:8000/admin/blog/category/2/change/)" 已经添加成功。你可以在下面添加其它的分类”。

这是因为我们没有给models中的类自定义`__str__`方法。可以为`typeidea\blog\models.py`的Category、Tag和Post等所有Model类，都添加类似如下的方法。

```
def __str__(self):
    return self.name
```

>  优化后：
>
> 新增分类操作成功后提示：“分类 "[测试](http://localhost:8000/admin/blog/category/3/change/)" 已经添加成功。你可以在下面添加其它的分类”。





##### 配置comnent应用



> typeidea\comment\admin.py

```
from django.contrib import admin

from .models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('target', 'nickname', 'content', 'website', 'created_time')
```



##### 配置config应用

> typeidea\config\admin.py

```
from django.contrib import admin

from .models import Link, SideBar


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'href', 'status', 'weight', 'created_time')
    fields = ('title', 'href', 'status', 'weight')

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(LinkAdmin, self).save_model(request, obj, form, change)


@admin.register(SideBar)
class SideBarAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_type', 'content', 'created_time')
    fields = ('title', 'display_type', 'content')

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(SideBarAdmin, self).save_model(request, obj, form, change)
```



至此，已经得到了一个基本可用的博客管理系统。

#### 2.4.2 订制admin

对于数据管理或者内容管理来说，我们需要操作的页面基本上只有两种：一种是数据批量展示和操作的列表页，与ModelAdmin相关；一种是数据增加或者修改的新增/编辑页，与ModelForm相关。



**（1）基于ModelAdmin**

##### 定义列表页

基于ModelAdmin的配置

> 痛点：权限问题
>
> 文章页面，当前登录的用户是A，但是却可以看到B用户的文章；
>
> 过滤器中展示了非当前用户创建的分类

**自定义过滤器**

> typeidea\blog\admin.py

```
# 原代码
list_filter = ['category']
```
以PostAdmin类为例：
```
    # 优化后
    class CategoryOwnerFilter(admin.SimpleListFilter):
        """
        自定义过滤器只展示当前用户的分类
        """
        title = '分类过滤器'
        parameter_name = 'owner_category'

        def lookups(self, request, model_admin):
            return Category.objects.filter(owner=request.user).values_list('id', 'name')

        def queryset(self, request, queryset):
            category_id = self.value()
            if category_id:
                return queryset.filter(category_id=self.value())
            return queryset

    list_filter = [CategoryOwnerFilter]
```

**自定义列表**

需求：解决权限问题，让当前登录的用户在列表页只能看到自己建的文章。

例如，在PostAdmin类中添加如下方法，可以修复文章列表的权限问题。

> typeidea\blog\admin.py

```
# 控制用户只能查看自己权限内的文章
def get_queryset(self, request):
    qs = super(PostAdmin, self).get_queryset(request)
    return qs.filter(owner=request.user)
```

完整代码：

> typeidea\blog\admin.py

```
from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import Category, Tag, Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'is_nav', 'post_count', 'created_time')  # 列表展示的字段
    fields = ('name', 'status', 'is_nav')  # 新增表单的条目

    # 重写ModelAdmin的save_model方法
    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(CategoryAdmin, self).save_model(request, obj, form, change)

    # 自定义函数：展示该分类有多少篇文章
    def post_count(self, obj):
        return obj.post_set.count()

    post_count.short_description = '文章数量'


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'created_time')  # 列表展示的字段
    fields = ('name', 'status')  # 新增表单的条目

    # 重写ModelAdmin的save_model方法
    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(TagAdmin, self).save_model(request, obj, form, change)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # ------ 列表页面：过滤器
    # 页面过滤器（默认展示在右侧）
    class CategoryOwnerFilter(admin.SimpleListFilter):
        """
        自定义过滤器只展示当前用户的分类
        """
        title = '分类过滤器'
        parameter_name = 'owner_category'

        def lookups(self, request, model_admin):
            return Category.objects.filter(owner=request.user).values_list('id', 'name')

        def queryset(self, request, queryset):
            category_id = self.value()
            if category_id:
                return queryset.filter(category_id=self.value())
            return queryset

    list_filter = [CategoryOwnerFilter]

    # ------ 列表页面：结果列部分表
    # 搜索框（在结果列表顶部，列表中的字段是表示支持检索的字段）
    search_fields = ['title', 'category__name']

    # 查询结果列表展示
    list_display = ['title', 'category', 'status', 'owner', 'created_time', 'operator']
    list_display_links = []

    # 在结果列表末尾加入一列，列名叫“操作”
    def operator(self, obj):
        return format_html('<a href="{}">编辑</a>', reverse('admin:blog_post_change', args=(obj.id,)))

    operator.short_description = '操作'

    # 针对列表的操作（默认展示在列表上/下侧位置）
    actions_on_top = True
    actions_on_bottom = True

    # ------ 新增编辑页面
    # 顶部是否展示保存按钮（默认是有一个在表单底部）
    save_on_top = True

    # 新增表单的内容
    fields = (
        ('title', 'category'),  # 嵌套元祖表示这几个字段在页面上处在同一排
        ('desc', 'status'),
        'content',
        'tag',
    )

    # 重写ModelAdmin的save_model方法
    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(PostAdmin, self).save_model(request, obj, form, change)

    # 控制用户只能查看自己权限内的文章
    def get_queryset(self, request):
        qs = super(PostAdmin, self).get_queryset(request)
        return qs.filter(owner=request.user)
```

综上，关于数据过滤的部分，只需要找到数据源在哪里，也就是QuerySet最终在哪里生成，然后对其进行一定的过滤即可实现效果。



##### 定义编辑页面

在新增/编辑页面中可以被订制的元素：

- 按钮：位置
- 输入框：样式
- 字段：顺序/是否可录/必填

按钮：在编辑页面中，最主要的是保存的功能按钮。Django默认提供了3个操作保存的按钮，分别是“保存”、“保存并增加另一个”和“保存并继续编辑”。

`save_on_top`控制是否在表单页面顶部展示3个保存按钮。

```
save_on_top = True	# 顶部也展示保存按钮
```

字段：可以通过`fields`来控制是否展示，以及展示的顺序和组合方式。通过`exclude`可以指定哪些字段是不展示的。字段列表中的嵌套元祖则表示这几个字段在页面上处在同一行。

> typeidea\blog\admin.py

```
exclude = ('owner',)

fields = (
        ('title', 'category'),  
        ('desc', 'status'),
        'content',
        'tag',
    )
```

也可以使用`fieldsets`来控制编辑页面的整体布局。注意，`fields`和`fieldsets`不能同时存在。

格式：

```
fieldsets = (
	(名称, {内容key, 内容value}),
	(名称, {内容key, 内容value}),
)
```

内容key的允许值有：description，fields和classes。其中，description是配置文本描述信息，fields是控制展示哪些字段，以及字段的排序和组合。classes是配置对应版块加CSS属性，Django默认支持的是`collapse`和`wide`，也可以自定义样式。

示例：

> typeidea\blog\admin.py

```
fieldsets = (
        ('文章基础配置', {
            'description': '这里是文章基础配置描述',
            'fields': (
                ('title', 'category'),
                'status',
            ),
        }),
        ('内容', {
           'fields': (
               'desc',
               'content',
           ),
        }),
        ('额外信息', {
            'classes': ('collapse',),
            'fields': ('tag', ),
        })
    )
```

关于编辑页的配置，还有针对多对多字段展示配置`filter_horizontal`和`filter_vertical`，用来控制多对多字段的展示效果。后续我们会通过其他插件来实现这种功能。

> typeidea\blog\admin.py

```
filter_horizontal = ('tag',)
filter_vertical = ('tag',)
```

![1606060812635](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\1606060812635.png)

##### 定义静态资源

可以通过自定义Media类来添加CSS样式和JS脚本。

> typeidea\blog\admin.py

```
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'created_time')  # 列表展示的字段
    fields = ('name', 'status')  # 新增表单的条目

    # 重写ModelAdmin的save_model方法
    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(TagAdmin, self).save_model(request, obj, form, change)
    
    class Media:
        css = {
            'all': ("https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css", ),
        }
        js = ('https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/js/bootstrap.bundle.js', )
```



**（2）基于ModelForm**



##### 自定义Form

需求：将文章的新增/编辑页面中的“摘要”的输入框，由input变成TextArea控件。

步骤1：在blog目录中创建`adminforms.py`文件。

> typeidea\blog\adminforms.py

```
from django import forms


class PostAdminForm(forms.ModelForm):
    desc = forms.CharField(widget=forms.Textarea, label='摘要', required=False)

```
步骤2：在`PostAdmin`中添加代码。
> typeidea\blog\admin.py

```
from .adminforms import PostAdminForm
......
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    ......
```



##### 混搭From

需求：在“分类”的编辑页面中，要能同时直接编辑“文章”（纳尼，还有这种操作？？？黑人问号脸）。

步骤1：新增一个`PostInline`类

> typeidea\blog\admin.py

```
class PostInline(admin.TabularInline):
    fields = ('title', 'desc')
    extra = 1	# 控制额外多挂几个
    model = Post
```

步骤2：在`CategoryAdmin`类中添加代码

```
inlines = [PostInline, ]
```



页面魔性效果

![1606063929959](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\1606063929959.png)

总之，对于需要在一个编辑页面内完成2个关联模型的编辑时，使用`inline admin`方式非常合适。



#### 2.4.3 订制site

一个url对应的时一个site，例如`url(r'^admin/', admin.site.urls)`。

大部分情况下，一个site对应一个站点就够用了。也可以通过订制site来实现一个系统对外提供多套admin后台逻辑。

需求：用户模块的管理，跟文章和分类等数据库的管理分开。

步骤1：创建`custom_site.py`文件

> typeidea\typeidea\custom_site.py

```
from django.contrib.admin import AdminSite


class CustomSite(AdminSite):
    site_header = 'Typeidea'
    site_title = 'Typeidea管理后台'
    index_title = '首页'


custom_site = CustomSite(name='cus_admin')
```

步骤2：修改所有app（blog/config/comment）的注册参数

```
from typeidea.custom_site import custom_site

# 修改前
@admin.register(Category)

# 修改后
@admin.register(Category, site=custom_site)

同理还有：
@admin.register(Tag, site=custom_site)
@admin.register(Post, site=custom_site)
@admin.register(Link, site=custom_site)
@admin.register(SideBar, site=custom_site)
@admin.register(Comment, site=custom_site)
```



对于PostAdmin，还要修改`operator`的对应代码。

```
# 修改前
def operator(self, obj):
    return format_html('<a href="{}">编辑</a>', reverse('admin:blog_post_change', args=(obj.id,)))

# 修改后
    def operator(self, obj):
        return format_html('<a href="{}">编辑</a>', reverse('cus_admin:blog_post_change', args=(obj.id,)))
```



步骤3：修改项目的路由配置

> typeidea\typeidea\urls.py

```
from django.conf.urls import url
from django.contrib import admin

from .custom_site import custom_site

urlpatterns = [
    url(r'^super_admin/', admin.site.urls),
    url(r'^admin/', custom_site.urls),
]
```

至此，我们就拥有了两套管理后台。一套用来管理用户，另一套用来管理业务。它们都是基于一套逻辑的用户系统，只是我们在url地址上进行了划分。



![1606065924666](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\1606065924666.png)

![1606065903200](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\1606065903200.png)

完整的PostAdmin代码

> typeidea\blog\admin.py

```
from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from typeidea.custom_site import custom_site
from .adminforms import PostAdminForm
from .models import Category, Tag, Post


class PostInline(admin.TabularInline):
    fields = ('title', 'desc')
    extra = 1
    model = Post


@admin.register(Category, site=custom_site)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'is_nav', 'post_count', 'created_time')  # 列表展示的字段
    fields = ('name', 'status', 'is_nav')  # 新增表单的条目

    # 重写ModelAdmin的save_model方法
    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(CategoryAdmin, self).save_model(request, obj, form, change)

    # 自定义函数：展示该分类有多少篇文章
    def post_count(self, obj):
        return obj.post_set.count()

    post_count.short_description = '文章数量'


@admin.register(Tag, site=custom_site)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'created_time')  # 列表展示的字段
    fields = ('name', 'status')  # 新增表单的条目

    # 重写ModelAdmin的save_model方法
    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(TagAdmin, self).save_model(request, obj, form, change)

    class Media:
        css = {
            'all': ("https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css",),
        }
        js = ('https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/js/bootstrap.bundle.js',)


@admin.register(Post, site=custom_site)
class PostAdmin(admin.ModelAdmin):
    # form = PostAdminForm

    # ------ 列表页面：过滤器
    # 页面过滤器（默认展示在右侧）
    class CategoryOwnerFilter(admin.SimpleListFilter):
        """
        自定义过滤器只展示当前用户的分类
        """
        title = '分类过滤器'
        parameter_name = 'owner_category'

        def lookups(self, request, model_admin):
            return Category.objects.filter(owner=request.user).values_list('id', 'name')

        def queryset(self, request, queryset):
            category_id = self.value()
            if category_id:
                return queryset.filter(category_id=self.value())
            return queryset

    list_filter = [CategoryOwnerFilter]

    # ------ 列表页面：结果列部分表
    # 搜索框（在结果列表顶部，列表中的字段是表示支持检索的字段）
    search_fields = ['title', 'category__name']

    # 查询结果列表展示
    list_display = ['title', 'category', 'status', 'owner', 'created_time', 'operator']
    list_display_links = []

    # 在结果列表末尾加入一列，列名叫“操作”
    def operator(self, obj):
        return format_html('<a href="{}">编辑</a>', reverse('admin:blog_post_change', args=(obj.id,)))

    operator.short_description = '操作'

    # 针对列表的操作（默认展示在列表上/下侧位置）
    actions_on_top = True
    actions_on_bottom = True

    # ------ 新增编辑页面
    # 顶部是否展示保存按钮（默认是有一个在表单底部）
    save_on_top = True

    # 新增表单的内容
    fields = (
        ('title', 'category'),  # 嵌套元祖表示这几个字段在页面上处在同一排
        ('desc', 'status'),
        'content',
        'tag',
    )

    filter_horizontal = ('tag',)  # 控制多对多字段的展示效果

    # 重写ModelAdmin的save_model方法
    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(PostAdmin, self).save_model(request, obj, form, change)

    # 控制用户只能查看自己权限内的文章
    def get_queryset(self, request):
        qs = super(PostAdmin, self).get_queryset(request)
        return qs.filter(owner=request.user)

```



#### 2.4.4 订制ModelAdmin

尽量避免冗余代码，降低后期维护成本。

抽象出一个`BaseOwnerAdmin`，为所有app服务。一是重写`save`方法，设置对象的`owner`；二是重写`get_queryset`方法，限定用户只能查看自己权限内的数据。



> typeidea\typeidea\BaseOwnerAdmin.py

```
from django.contrib import admin


class BaseOwnerAdmin(admin.ModelAdmin):
    exclude = ('owner',)

    def get_queryset(self, request):
        qs = super(BaseOwnerAdmin, self).get_queryset(request)
        return qs.filter(owner=request.user)

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(BaseOwnerAdmin, self).save_model(request, obj, form, change)
```

然后更新`blog`应用的`admin`代码

> typeidea\blog\admin.py

```
from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from typeidea.custom_site import custom_site
from typeidea.BaseOwnerAdmin import BaseOwnerAdmin
from .models import Category, Tag, Post


class CategoryOwnerFilter(admin.SimpleListFilter):
    title = '分类过滤器'
    parameter_name = 'owner_category'

    def lookups(self, request, model_admin):
        return Category.objects.filter(owner=request.user).values_list('id', 'name')

    def queryset(self, request, queryset):
        category_id = self.value()
        if category_id:
            return queryset.filter(category_id=self.value())
        return queryset


@admin.register(Category, site=custom_site)
class CategoryAdmin(BaseOwnerAdmin):
    list_display = ('name', 'status', 'is_nav', 'post_count', 'created_time')  # 列表展示的字段
    fields = ('name', 'status', 'is_nav')  # 新增表单的条目

    # 自定义函数：展示该分类有多少篇文章
    def post_count(self, obj):
        return obj.post_set.count()

    post_count.short_description = '文章数量'


@admin.register(Tag, site=custom_site)
class TagAdmin(BaseOwnerAdmin):
    list_display = ('name', 'status', 'created_time')  # 列表展示的字段
    fields = ('name', 'status')  # 新增表单的条目

    # 重写ModelAdmin的save_model方法
    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(TagAdmin, self).save_model(request, obj, form, change)

    class Media:
        css = {
            'all': ("https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css",),
        }
        js = ('https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/js/bootstrap.bundle.js',)


@admin.register(Post, site=custom_site)
class PostAdmin(BaseOwnerAdmin):
    # ------ 列表页面
    list_display = ['title', 'category', 'status', 'owner', 'created_time', 'operator']
    list_display_links = []

    # 在结果列表末尾追加一列字段，列名叫“操作”
    def operator(self, obj):
        return format_html('<a href="{}">编辑</a>', reverse('cus_admin:blog_post_change', args=(obj.id,)))

    operator.short_description = '操作'

    actions_on_top = True  # 动作按钮
    actions_on_bottom = True  # 动作按钮

    search_fields = ['title', 'category__name']  # 搜索框（列表元素是可支持检索的字段）
    list_filter = [CategoryOwnerFilter]  # 过滤器

    # ------ 新增编辑页面
    save_on_top = True      # 保存按钮三连

    # 新增表单的内容
    fields = (
        ('title', 'category'),  # 嵌套元祖表示这几个字段在页面上处在同一排
        ('desc', 'status'),
        'content',
        'tag',
    )

    filter_horizontal = ('tag',)    # 横排展示多对多字段

```

> typeidea\config\admin.py

```
from django.contrib import admin
from typeidea.custom_site import custom_site
from typeidea.BaseOwnerAdmin import BaseOwnerAdmin
from .models import Link, SideBar


@admin.register(Link, site=custom_site)
class LinkAdmin(BaseOwnerAdmin):
    list_display = ('title', 'href', 'status', 'weight', 'created_time')
    fields = ('title', 'href', 'status', 'weight')


@admin.register(SideBar, site=custom_site)
class SideBarAdmin(BaseOwnerAdmin):
    list_display = ('title', 'display_type', 'content', 'created_time')
    fields = ('title', 'display_type', 'content')
```



#### 2.4.5 记录操作日志

LogEntry也是后台开发中经常用到的模块，它在admin后台是默认开启的。

日志记录的功能ModelAdmin本身就有，当我们新增一个实体对象（Post,Category,Tag等）时，它就会帮我们记录一条变更记录。当我们修改一条记录时，它又会帮我们调用LogEntry来创建一条操作日志。

ModelAdmin内部提供了两个方法，分别是`log_addition`和`log_change`，可以在`django/admin/contrib/options.py`文件中查阅具体代码。

支持的参数：

| 参数            | 说明                                        |
| --------------- | ------------------------------------------- |
| user_id         | 当前用户id                                  |
| content_type_id | 要保存内容的类型                            |
| object_id       | 记录变更示例的id                            |
| object_repr     | 实例的展示名称，即`__str__`方法所返回的内容 |
| action_flag     | 操作标记                                    |
| change_message  | 记录的消息                                  |

查询某个对象的变更

```
from django.contrib.admin.models import LogEntry, CHANGE
from django.contrib.admin.options import get_content_type_for_model

post = Post.objects.get(id=1)
log_entries = LogEntry.objects.filter(
	content_type_id = get_content_type_for_mode(post).pk,
	object_id = post.id,
)
```



在admin页面上查看操作日志

> typeidea\blog\admin.py

```
......

from django.contrib.admin.models import LogEntry


@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    list_display = ['object_repr', 'object_id', 'action_flag', 'user', 'change_message']
```

备注：按理这部分代码放在`typeidea\typeidea\admin.py`中会更合适，此处只做体验。页面会被注册到超级管理员的后台页面中，访问地址是`http://localhost:8000/super_admin/`

![1606148823435](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\1606148823435.png)

![1606148846547](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\1606148846547.png)





### 2.5 开发前端界面

























### 2.6 Bootstrap





## 三、第三方插件





### 四、API







## 五、上线

