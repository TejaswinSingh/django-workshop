from django.urls import path
from .import views

app_name = 'articles'

urlpatterns = [
    path('check/', views.check, name="check"),
    path('', views.home, name="home"),
    path('article/<int:article_id>/', views.article_page, name="article_page"),
    path('add_comment/<int:article_id>/', views.add_comment, name="add_comment"),
]