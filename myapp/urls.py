from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, TaskCreateView, TaskUpdateView, TaskDeleteView, TaskToggleView

# Create router and register our viewset
router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='tasks')

urlpatterns = [
    path('', include(router.urls)),  # REST API: /api/tasks/
    path('tasks/add/', TaskCreateView.as_view(), name="task-create"),  # Create task
    path('tasks/update/<int:pk>/', TaskUpdateView.as_view(), name="task-update"),  # Update task
    path('tasks/delete/<int:pk>/', TaskDeleteView.as_view(), name="task-delete"),  # Delete task
    path('tasks/toggle/<int:pk>/', TaskToggleView.as_view(), name="task-toggle"),  # Toggle completion status
]
