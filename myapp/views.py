from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Task
from .serializers import TaskSerializer

@api_view(['GET'])
def get_tasks(request):
    """
    Fetch all tasks.
    """
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def add_task(request):
    """
    Add a new task.
    """
    serializer = TaskSerializer(data=request.data)
    
    # Check if the data provided is valid
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    # Return errors if the data is invalid
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_task(request, pk):
    """
    Delete a task by its ID.
    """
    try:
        task = Task.objects.get(pk=pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Task.DoesNotExist:
        # Return 404 if the task is not found
        return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
def update_task(request, pk):
    """
    Update an existing task.
    """
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        # Return 404 if the task is not found
        return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)
    
    # Deserialize the incoming data
    serializer = TaskSerializer(task, data=request.data)
    
    # Validate and save the updated task
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    
    # Return errors if the data is invalid
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
