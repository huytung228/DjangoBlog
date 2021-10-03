from django.db.models import fields
from django.forms import ModelForm
from .models import Article

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'slug', 'body', 'thumb']