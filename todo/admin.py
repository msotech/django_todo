from django.contrib import admin

from todo.models import ToDo


@admin.register(ToDo)
class ToDoAdmin(admin.ModelAdmin):
    list_display = ("title", "completed")
    list_filter = ("completed",)
    search_fields = ("title", "description")
    ordering = ("completed", "title")