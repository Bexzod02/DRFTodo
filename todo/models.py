from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=211)
    description = models.TextField()
    completed = models.BooleanField(default=False)
