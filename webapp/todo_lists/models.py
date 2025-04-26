from django.db import models

# Create your models here.

from django.contrib.auth.models import User # new
 
 # Create your models here.
class TodoList(models.Model):
    name = models.CharField('To-do list name', max_length=100, null=False, blank=False)
    # Dokumentacja z przykładem relacji jeden-do-wielu: https://docs.djangoproject.com/en/5.1/topics/db/examples/many_to_one/
    owner = models.ForeignKey(User, on_delete=models.CASCADE)