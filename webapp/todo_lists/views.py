from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
 
from todo_lists.forms import TodoListForm
from todo_lists.models import TodoList
 # Create your views here.
@login_required
def index(request):
     lists = (TodoList
              .objects
              .filter(owner=request.user)
              .order_by('-id'))
     return render(request, 'todo_lists/index.html', {'lists': lists})

@login_required
def create(request):
    error = ''
 
    if request.method == 'POST':
        form = TodoListForm(request.POST)
        if form.is_valid():
            # Na tym etapie definiujemy, że każda lista powiązana jest z jej autorem, czyli zalogowanym użytkownikiem
            form.instance.owner = request.user
            form.save()
            return redirect('todo-lists')
        else:
            error = 'Submitted form contain errors'
 
 
    form = TodoListForm()
 
    data = {
        'form': form,
        'error': error,
    }
    return render(request, 'todo_lists/create.html', data)