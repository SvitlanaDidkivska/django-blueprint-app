from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponseNotAllowed
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required 

# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    elif request.method == "GET":
        form = UserCreationForm()
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])
    return render(request,'auth/register.html', {'form':form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')
    elif request.method == 'GET':
        form = AuthenticationForm()
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])
    
    return render(request,'auth/login.html', {'form':form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('home')


