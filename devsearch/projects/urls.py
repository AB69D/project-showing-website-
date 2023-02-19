from django.urls import path
from . import views


urlpatterns = [
    path('', views.projects,name='projects'),
    path('project/<str:pk>/', views.single_project,name='project'),
    path('create/', views.create_project,name='createproject'),
    path('update/<str:pk>', views.update_project,name='updateproject'),
    path('delete/<str:pk>', views.delete_project,name='delete'),
]
