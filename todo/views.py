from django.http import HttpRequest, JsonResponse, HttpResponse
from django.shortcuts import render
from rest_framework import viewsets, status
from todo.models import Todo, TodoList
from todo.serializers import TodoSerializer, TodoListSerializer
from rest_framework.permissions import IsAuthenticated


class TodoViewSet(viewsets.ModelViewSet):
    
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated, )
    filterset_fields = ['due_date', 'favourite', 'completed']


class TodoListViewSet(viewsets.ModelViewSet):
    
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer
    permission_classes = (IsAuthenticated, )

def hello_world(request: HttpRequest, name: str):
    if request.user.is_anonymous:
        return HttpResponse(status=status.HTTP_403_FORBIDDEN)
    if request.method == 'GET':
        # print(request.GET['age'])
        return JsonResponse({'message': f'Hello, {name}!'})
    else:
        return HttpResponse( status=status.HTTP_405_METHOD_NOT_ALLOWED)

      