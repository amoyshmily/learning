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


