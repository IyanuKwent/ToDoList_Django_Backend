from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from myapp.views import TaskViewSet
from django.http import JsonResponse  # for default root response

# Create router and register our viewset
router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

# Simple view for root URL
def index(request):
    return JsonResponse({'message': 'Welcome to the Django API'})

# URL patterns
urlpatterns = [
    path('', index),  # 👈 Shows a JSON response at http://127.0.0.1:8000/
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # 👈 REST API endpoint at /api/tasks/
    path('api-auth/', include('rest_framework.urls')),  # 👈 Optional login/logout for browsable API
]
