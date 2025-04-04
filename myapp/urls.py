# urls.py in your Django app
from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.TaskListView.as_view(), name='task-list'),
    path('tasks/add/', views.TaskCreateView.as_view(), name='task-add'),
    path('tasks/update/<int:pk>/', views.TaskUpdateView.as_view(), name='task-update'),
    path('tasks/toggle/<int:pk>/', views.TaskToggleView.as_view(), name='task-toggle'),
    path('tasks/delete/<int:pk>/', views.TaskDeleteView.as_view(), name='task-delete'),
]
