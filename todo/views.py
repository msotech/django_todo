from rest_framework import generics

from todo.models import ToDo
from todo.serializers import ToDoSerializer

class TodoListView(generics.ListAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer