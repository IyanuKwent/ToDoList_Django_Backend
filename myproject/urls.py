from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from myapp.views import TaskViewSet

# Restrict allowed methods in the viewset
class TaskViewSetRestricted(TaskViewSet):
    http_method_names = ['get', 'post', 'put', 'delete']

router = DefaultRouter()
router.register(r'tasks', TaskViewSetRestricted, basename='task')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # Automatically includes only specified CRUD routes
]
