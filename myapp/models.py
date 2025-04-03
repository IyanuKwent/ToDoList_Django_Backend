from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Task(models.Model):
    task = models.CharField(max_length=255)  # Task description
    completed = models.BooleanField(default=False)  # Task status

    def __str__(self):
        return self.task