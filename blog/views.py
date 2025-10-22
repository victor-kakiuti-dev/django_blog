from django.shortcuts import render
from utils.blog.factory import make_article

def home(request):
    return render(request, 'blog/pages/home.html', context={
        'article': [make_article() for _ in range(10)]
    })

def article(request, id):
    return render(request, 'blog/pages/article_view.html', context={
            'articles': make_article(),
            'is_detail_page': True,
    })

# Create your views here.
