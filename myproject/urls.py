from django.urls import path, include
from rest_framework.routers import DefaultRouter
from myapp.views import TaskViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('api/tasks/', include('myapp.urls')),  # Correct URL
]
