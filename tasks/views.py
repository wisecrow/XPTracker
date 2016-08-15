from django.shortcuts import render
from tasks.forms import TaskForm


def show_index(request, id):
    form = TaskForm()
    return render(request, 'tasks.html',
                  {'title':'Tasks',
                      'form': form})