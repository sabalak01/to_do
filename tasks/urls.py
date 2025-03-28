from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('new/', views.create_task,name='create_task'),
]