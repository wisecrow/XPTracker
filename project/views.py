# import re

from django.core.exceptions import ValidationError

from django.http import HttpResponseNotFound


from django.shortcuts import redirect, render


from project.models import Project

from project.forms import ProjectForm


def show_index(request):
    return redirect('/projects/')


def new_project(request):
    if request.method == 'POST':
        identifier = request.POST.get('identifier', '')
        p1 = Project(
            title=request.POST.get('title', ''),
            description=request.POST.get('description', ''),
            release_date=request.POST.get('release_date', ''),
            identifier=identifier
        )
        try:
            # run for SQLite validation enforcement
            p1.full_clean()
            p1.save()
            return redirect(p1)
        except ValidationError:
            pass

    return redirect('show_projects')


def show_projects(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {
        'title': 'Projects',
        'form': ProjectForm,
        'projects': projects})


def show_project(request, id):
    project = Project.objects.filter(identifier=id)
    if not project:
        return HttpResponseNotFound('Page not found!')
    return render(request, 'project.html', {'project': project[0]})


# def get_url_string(title):
#  return re.sub(
#     r'[^a-zA-Z0-9]', ' ', title).strip().replace(' ', '-').lower()
