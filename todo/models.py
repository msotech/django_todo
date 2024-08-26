from django.db import models

# Create your models here.

class ToDo(models.Model):
    title = models.CharField( max_length=120 )
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)