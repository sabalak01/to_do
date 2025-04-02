from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('new/', views.create_task,name='create_task'),
    path('task/<int:task_id>/complete', views.complete_task, name='complete_task'),
    path('task/<int:task_id>', views.task_description, name='task_description'),
    path('task/<int:task_id>/delete', views.delete_task,name='delete_task'),
]