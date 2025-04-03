from django.urls import path
from .views import get_tasks, add_task, delete_task, update_task

urlpatterns = [
    path('', get_tasks, name='get_tasks'),  # Matches '/api/'
    path('add/', add_task, name='add_task'),  # Matches '/api/add/'
    path('delete/<int:pk>/', delete_task, name='delete_task'),
    path('update/<int:pk>/', update_task, name='update_task'),
]
