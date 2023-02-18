from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.projects,name='projects'),
    path('project/<str:pk>/', views.single_project,name='project'),
]
