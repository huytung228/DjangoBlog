from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.article_list, name='list'),
    path('create', views.create_article, name='create'),
    path('<slug_article>', views.article_detail, name='detail'),
    path('delete/<article_delete>', views.article_delete, name='delete'),
    path('edit/<article_edit>', views.article_edit, name='edit')
]
