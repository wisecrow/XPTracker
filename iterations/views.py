from django.shortcuts import render
from iterations.forms import IterationForm
from project.models import Project
from django.http import HttpResponseNotFound

def show_index(request, id):
    projects = Project.objects.filter(identifier=id)
    if not projects:
        raise HttpResponseNotFound

    form = IterationForm(projectid=projects[0].id)
    return render(request, 'iterations.html', {
        'title': 'Iterations',
        'form': form
        })
