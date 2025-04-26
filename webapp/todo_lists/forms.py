from .models import TodoList
from django.forms import ModelForm, TextInput, IntegerField
 
 
class TodoListForm(ModelForm):
 
    class Meta:
        model = TodoList
        fields = ['name']
 
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'To-do list name'}),
        }