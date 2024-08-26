from rest_framework import generics

from todo.models import ToDo
from todo.serializers import ToDoSerializer

class TodoListCreateView(generics.ListCreateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

class TodoView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

