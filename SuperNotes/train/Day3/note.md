
## 课程标题：发布博客文章

#### 课程内容
```
一、课程目标

1.了解model的编写方法
2.掌握数据迁移方法
3.配置超级管理员及其管理界面

二、知识点

1.编写实体类
目标文件：/blog/models.py

代码内容：
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class MyBlog(models.Model):
    """
    定义博客实体类的字段
    """
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()
    publish_tm = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-publish_tm', )    # 排序

    def __str__(self):
        return self.title

2.数据迁移
在manage.py所在目录中，依次执行以下指令：
python manage.py makemigrations

python manage.py migrate

三、管理界面

1.创建超级管理员账号
在manage.py所在目录中，执行以下指令：
python manage.py createsuperuser
然后，按照指引，依次设定超级管理员的用户名、邮箱和密码。

2.自定义界面内容
目标文件：/blog/admin.py
代码内容：
from django.contrib import admin
from .models import MyBlog

admin.site.register(MyBlog)

3.丰富博客展示信息
目标文件：/blog/admin.py
代码内容：
from django.contrib import admin
from .models import MyBlog

class MyBlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish_tm')
    list_filter = ('publish_tm', 'author')
    search_fields = ('title', 'body')
    raw_id_fields = ('author', )
    date_hierarchy = 'publish_tm'
    ordering = ['-publish_tm', 'author']

admin.site.register(MyBlog, MyBlogAdmin)

4.登录博客网站，发布一篇博客
步骤1：在manage.py所在目录中，执行指令：
python manage.py runserver 来启动博客web应用。

步骤2：访问地址localhost:8000/admin
当页面提示登录时，输入之前创建好的超级管理员账号和密码，执行登录

步骤3：发布一条博客
在【BLOG】栏目中，点击“+添加”，输入Title、Author、Body等信息，然后点击“保存”即可。

四、补充知识

1.sqlite的基本操作指令
指令：sqlite3 db.sqlite3  启动sqlite3
指令：.tables     查看现有表

备注：请在sqlite3文件所在目录中打开cmd窗口，然后执行对应指令。
查看sqlite3的数据库和表内容，除了上述的命令行方式外，还可以下载可视化工具，例如
SQLite studio 或者 Navicat for SQLite工具。
```