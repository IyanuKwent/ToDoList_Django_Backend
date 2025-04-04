from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from myapp.views import TaskViewSet
from django.http import JsonResponse

# Create router and register our viewset
router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='tasks')

# Root JSON welcome message
def index(request):
    return JsonResponse({'message': 'Welcome to the Django API'})

# URL patterns
urlpatterns = [
    path('', index),  # Root index
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # Register the TaskViewSet for /api/tasks/
    path('api-auth/', include('rest_framework.urls')),  # Optional login/logout
]
