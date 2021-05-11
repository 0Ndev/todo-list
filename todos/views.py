from django import forms
from django.shortcuts import render
from .models import Todos
from .forms import TodoForm


# def index(request):
#     return render(request, 'index.html')


def todo_list(request):
    tasks = Todos.objects.all()

    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()

    # return render(request, 'todo-list.html', {'tasks': tasks, 'form': form})
    return render(request, 'index.html', {'tasks': tasks, 'form': form})
