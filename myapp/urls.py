from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.get_tasks, name='get_tasks'),
    path('tasks/add/', views.add_task, name='add_task'),
    path('tasks/update/<int:id>/', views.update_task, name='update_task'),
    path('tasks/delete/<int:id>/', views.delete_task, name='delete_task'),
    path('tasks/toggle/<int:id>/', views.toggle_task, name='toggle_task'),
]
