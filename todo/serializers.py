from rest_framework import serializers
from todo.models import ToDo

class TodoSerializer(serializers.Modelserializer):
    class Meta:
        model = ToDo
        fields = "__all__"