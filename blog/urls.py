from blog.views import home, contato
from django.urls import path



urlpatterns = [
    path('', home),
    path('contato/', contato),
]