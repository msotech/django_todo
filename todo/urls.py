from django.urls import path

from todo.views import ToDoCreateListView, ToDoView

urlpatterns = [
    path("", ToDoCreateListView.as_view(), name="todo-list"),
    path("<int:pk>/", ToDoView.as_view(), name="todo-detail")
]
