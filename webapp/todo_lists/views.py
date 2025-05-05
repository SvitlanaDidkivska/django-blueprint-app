from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import DetailView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from todo_lists.forms import TodoListForm, TaskForm
from todo_lists.models import TodoList, Task
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

# optionalTODO: Należy poszukać sposób naprawy błędu o nazwie N+1 dla wyświetlania zadań z listy
class TodoListDetailView(LoginRequiredMixin, DetailView):
    model = TodoList
    template_name = 'todo_lists/show.html'
    context_object_name = 'todo_list'
 
def createTask(request, pk):

    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.instance.todo_list = TodoList.objects.get(id=pk)
            form.save()
        return redirect('show-todo-list', pk=pk)
    form = TaskForm()
 
    data = {
         'form': form,
    }
    return render(request, 'todo_lists/create_task.html', data)

def checkTask(request, pk, task_id):
    task = Task.objects.get(id=task_id)
    task.is_completed = True
    task.save()
    return redirect('show-todo-list', pk=pk)
 
def uncheckTask (request, pk, task_id):
    task = Task.objects.get(id=task_id)
    task.is_completed = False
    task.save()
    return redirect('show-todo-list', pk=pk)

class TaskDeleteView(DeleteView):
     model = Task
     template_name = 'todo_lists/delete_task.html'
     success_url = '/todo-lists/'