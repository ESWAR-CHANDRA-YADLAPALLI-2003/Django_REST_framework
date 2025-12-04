# api_app/models.py
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(unique=True)
    roll_no = models.CharField(max_length=30, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.roll_no})"
