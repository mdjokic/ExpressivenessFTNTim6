from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('visualization/', views.visualization, name="visualization"),
    path('getGraph/', views.getGraph, name='getGraph'),
    path('uploadData/', views.uploadData, name='uploadData'),
    path('saveData/', views.saveData, name='saveData')
]