# import re

from django.core.exceptions import ValidationError

from django.http import HttpResponseNotFound


from django.shortcuts import redirect, render


from project.models import Project

from project.forms import ProjectForm


def show_index(request):
    return redirect('/projects/')


def new_project(request):
    form = ProjectForm(data=request.POST)
    if form.is_valid():
        project = form.save()
        return redirect(project)

    return render(request, 'projects.html', {'form': form})


def show_projects(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {
        'title': 'Projects',
        'form': ProjectForm(),
        'projects': projects})


def show_project(request, id):
    project = Project.objects.filter(identifier=id)
    if not project:
        return HttpResponseNotFound('Page not found!')
    return render(request, 'project.html', {'project': project[0]})


# def get_url_string(title):
#  return re.sub(
#     r'[^a-zA-Z0-9]', ' ', title).strip().replace(' ', '-').lower()
