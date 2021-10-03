from django.db import models
from django.db.models.fields import DateField
from django.urls.converters import SlugConverter
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField(default='')
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png')
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title

    def snippet(self):
        return self.body[:50] + '...'
