from django.urls import path

from todo.views import TodoListCreateView, TodoView

urlpatterns = [
    path("", TodoListCreateView.as_view(), name="todo-list"),
    path("<int:pk>/", TodoView.as_view(), name="todo-edit")
]
