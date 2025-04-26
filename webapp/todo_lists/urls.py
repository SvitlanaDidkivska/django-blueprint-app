# Plik do zarządzania ścieżkami w aplikacji. Zawiera listę ścieżek powiązanych z widokami.
 
from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.index, name='todo-lists'),
    path('create', views.create, name='create-todo-list'),
    path('<int:pk>', views.TodoListDetailView.as_view(), name='show-todo-list'),
]