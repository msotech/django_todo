from django import forms 
from todo.models import ToDo

class ToDoForm(forms.ModelForm):
    
    class Meta:
        model = ToDo
        fields = ["title", "description", "completed"]