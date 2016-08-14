from django.shortcuts import render, redirect
from iterations.forms import IterationForm
from project.models import Project
from django.http import HttpResponseNotFound
from iterations.models import Iteration

def retrieve_project(id):
    projects = Project.objects.filter(identifier=id)
    if not projects:
        raise Exception
    return projects[0]

def show_index(request, id):
    project = retrieve_project(id)
    iterations = Iteration.objects.filter(project=project)
    form = IterationForm(projectid=project.id)
    return render(request, 'iterations.html', {
        'title': 'Iterations',
        'form': form,
        'iterations': iterations,
        'project_id': project.identifier
        })

def create_new(request, id):
    project = retrieve_project(id)
    form = IterationForm(data=request.POST, projectid=project.id)
    if form.is_valid():
        form.save(project)
        return redirect('/projects/%s/iterations/' % id)
    return render(request, 'iterations.html', {
        'title': 'Iterations',
        'form': form,
        'project_id': project.identifier
        })