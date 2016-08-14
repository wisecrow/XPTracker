# import re

from django.core.exceptions import ValidationError

from django.http import HttpResponseNotFound


from django.shortcuts import redirect, render


from project.models import Project

from project.forms import ProjectForm

from user_stories.models import UserStory


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
    projects = Project.objects.filter(identifier=id)
    user_stories = UserStory.objects.filter(project=projects[0])
    if not projects:
        return HttpResponseNotFound('Page not found!')
    return render(request, 'project.html', {
        'project': projects[0],
        'user_stories': user_stories})


# def get_url_string(title):
#  return re.sub(
#     r'[^a-zA-Z0-9]', ' ', title).strip().replace(' ', '-').lower()
