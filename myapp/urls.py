from django.urls import path
from myapp.views import TaskListView, AddTaskView, UpdateTaskView, DeleteTaskView, ToggleTaskView

urlpatterns = [
    path('tasks/', TaskListView.as_view(), name='get_tasks'),
    path('tasks/add/', AddTaskView.as_view(), name='add_task'),
    path('tasks/update/<int:id>/', UpdateTaskView.as_view(), name='update_task'),
    path('tasks/delete/<int:id>/', DeleteTaskView.as_view(), name='delete_task'),
    path('tasks/toggle/<int:id>/', ToggleTaskView.as_view(), name='toggle_task'),
]
