from django.contrib import admin
from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    # /posts/createにアクセスした時にCreateViewsを呼び出す
    path('create/', views.CreateView.as_view(), name='create'),
]