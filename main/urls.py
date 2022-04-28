from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('', views.index, name='index'),
    path('demo', views.demo, name='demo'),
    path('editor', views.editorPage, name='editorPage'),
    path('auth', views.authPage, name='auth')
]
