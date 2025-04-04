from django.contrib import admin
from django.urls import path
from django.http import JsonResponse
from myapp.views import (
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TaskToggleView,
)

# Simple view for root URL
def index(request):
    return JsonResponse({'message': 'Welcome to the Django API'})

# URL patterns
urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),

    # Custom API views
    path('api/tasks/', TaskListView.as_view()),
    path('api/tasks/add/', TaskCreateView.as_view()),
    path('api/tasks/update/<int:id>/', TaskUpdateView.as_view()),
    path('api/tasks/delete/<int:id>/', TaskDeleteView.as_view()),
    path('api/tasks/toggle/<int:id>/', TaskToggleView.as_view()),
]
