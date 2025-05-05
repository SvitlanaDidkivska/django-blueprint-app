from django.db import models

# Create your models here.

from django.contrib.auth.models import User # new
 
 # Create your models here.
class TodoList(models.Model):
    name = models.CharField('To-do list name', max_length=100, null=False, blank=False)
    # Dokumentacja z przykładem relacji jeden-do-wielu: https://docs.djangoproject.com/en/5.1/topics/db/examples/many_to_one/
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    def is_completed(self):
        return not self.task_set.filter(is_completed=False).exists()
 
    def is_empty(self):
        return not self.task_set.all().exists()

class Task(models.Model):
     name = models.CharField('Task name', max_length=100, null=False, blank=False)
     # Lista wszystich dostępnych typów danych dostępna jest w dokumentacji: https://docs.djangoproject.com/en/5.2/ref/models/fields/#field-types
     is_completed = models.BooleanField('Task completion indicator', default=False, null=False, blank=False)
     # Dokumentacja z przykładem relacji jeden-do-wielu: https://docs.djangoproject.com/en/5.1/topics/db/examples/many_to_one/
     todo_list = models.ForeignKey(TodoList, on_delete=models.CASCADE)