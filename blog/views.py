from django.shortcuts import render
from utils.blog.factory import make_article
from .models import Article


def home(request):
    articles = Article.objects.filter(
        is_published=True,
    ).order_by('-id')
    return render(request, 'blog/pages/home.html', context={
        'article': articles,
    })

def article(request, id):
    article = Article.objects.filter(
        is_published=True,
    ).order_by('-id').first()
    return render(request, 'blog/pages/article_view.html', context={
            'articles': article,
            'is_detail_page': True,
    })


