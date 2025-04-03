from django.shortcuts import render
from django.http import JsonResponse  # Import JsonResponse for the home view

from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer
from rest_framework.decorators import api_view

def home_view(request):
    """Return a welcome message."""
    return JsonResponse({'message': 'Welcome to the API!'})  # Simple welcome message

@api_view(['POST'])
def add_task(request):
    if request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Save the new task to the database
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

class TaskViewSet(viewsets.ModelViewSet):

    queryset = Task.objects.all()
    serializer_class = TaskSerializer