from django.shortcuts import render
from .models import MyBlog


def blog_title(request):
    blogs = MyBlog.objects.all()
    return render(request, 'blog/titles.html', {'blogs': blogs})


def blog_article(request, article_id):
    article = MyBlog.objects.get(id=article_id)
    pub = article.publish_tm
    return render(request, 'blog/article.html', {'article': article, 'publish_tm': pub})
