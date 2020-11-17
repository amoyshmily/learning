# Django 学习笔记



## 初入江湖

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

## 小试牛刀

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

