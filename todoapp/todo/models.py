from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class Author(models.Model):
#     firstname = models.CharField(max_length=64)
#     lastname = models.CharField(max_length=64)
    
#     def __str__(self):
#         return f"{self.firstname} {self.lastname}"

# class Task(models.Model):
#     text = models.CharField(max_length=255)
#     status = models.BooleanField(default=False)
#     # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todo")
#     def __str__(self):
#         return f"{self.text}"

class Task(models.Model):
    text = models.CharField(max_length=255)
    status = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="task")
    def __str__(self):
        return f"{self.text}"