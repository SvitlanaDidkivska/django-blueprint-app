from django.db import models

# Create your models here.

from django.contrib.auth.models import User # new
 
 # Create your models here.
class TodoList(models.Model):
    name = models.CharField('To-do list name', max_length=100, null=False, blank=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)