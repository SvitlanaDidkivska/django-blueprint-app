from .models import TodoList, Task
from django.forms import ModelForm, TextInput, IntegerField
 
 
class TodoListForm(ModelForm):
 
    class Meta:
        model = TodoList
        fields = ['name']
 
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'To-do list name'}),
        }

class TaskForm(ModelForm):
 
     class Meta:
         model = Task
         fields = ['name']
 
         widgets = {
             'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Task name'}),
         }