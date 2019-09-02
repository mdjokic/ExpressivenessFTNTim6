from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('createGraph/', views.createGraph, name='createGraph')
]