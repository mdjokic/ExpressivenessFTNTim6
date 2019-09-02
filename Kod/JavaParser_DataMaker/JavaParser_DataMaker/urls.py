from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('project_upload/', views.project_upload, name='project_upload')
    #path('project_upload/', views.FileFieldView.as_view(), name='project_upload')
]