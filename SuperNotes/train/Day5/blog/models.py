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
        ordering = ('-publish_tm',)  # 排序

    def __str__(self):
        return self.title
