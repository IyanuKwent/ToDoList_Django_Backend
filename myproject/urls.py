from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
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
    path('', index),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)), 
    path('api-auth/', include('rest_framework.urls')),
    path('api/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
