from django.urls import path
from . import views


app_name = 'news'
urlpatterns = [
    path('', views.news_home, name='blog'),
    path('add', views.work, name='work'),
    path('<int:pk>', views.NewsDetailView.as_view(), name='news-detail'),


]
