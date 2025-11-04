from django.db import models
from django.contrib.auth.models import User
 

class Article(models.Model):
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=165)
    slug = models.SlugField()
    article = models.TextField()
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
    )
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title