from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import Taskserializers
from .models import Task

#this view for task lists

@api_view(['GET'])
def taskList(self,request,format=None):
    tasks = Task.objects.all()
    serializer = self.Taskserializer(tasks, many = True)
    return Response(serializer.data)

# this view for task detail"

@api_view(['GET'])
def taskDetail(request, pk):
    tasks = Task.objects.get(id=pk)
    serializer = Taskserializer(tasks, many = False)
    return Response(serializer.data)

#this view update a list


@api_view(['POST'])
def taskUpdate(request, pk):
    task = Task.objects.get(id = pk)
    serializer = Taskserializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

#this view for create a task

@api_view(['POST'])
def taskCreate(request):
    serializer = Taskserializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

#this view for delete a task

@api_view(['DELETE'])
def taskDelete(request, pk):
    task = Task.objects.get(id = pk)
    task.delete()
    return Response("Taks deleted successfully.")

# Create your views here.
