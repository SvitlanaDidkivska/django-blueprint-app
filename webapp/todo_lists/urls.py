# Plik do zarządzania ścieżkami w aplikacji. Zawiera listę ścieżek powiązanych z widokami.
 
from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.index, name='todo-lists'),
    path('create', views.create, name='create-todo-list'),
    path('<int:pk>', views.TodoListDetailView.as_view(), name='show-todo-list'),
    path('<int:pk>/create', views.createTask, name='create-task'),
    path('<int:pk>/<int:task_id>/check', views.checkTask, name='check-task'),
    path('<int:pk>/<int:task_id>/uncheck', views.uncheckTask, name='uncheck-task'),
    path('<int:list_id>/<int:pk>/delete', views.TaskDeleteView.as_view(), name='delete-task'),
]