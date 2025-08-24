from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=512)
    description = models.TextField()
    index = models.IntegerField(default=0)
    due_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    

    def __str__(self):
        return self.title
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name
