from django.shortcuts import render
from django.http import JsonResponse  # Import JsonResponse for the home view

from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer

def home_view(request):
    """Return a welcome message."""
    return JsonResponse({'message': 'Welcome to the API!'})  # Simple welcome message

class TaskViewSet(viewsets.ModelViewSet):

    queryset = Task.objects.all().order_by('-created_at')  # Fetch all tasks
    serializer_class = TaskSerializer