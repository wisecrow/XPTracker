from django.http import  HttpResponseNotFound

from django.shortcuts import render, redirect

from django.http import HttpResponse

from user_stories.models import UserStory

from user_stories.forms import UserStoryForm

from project.models import Project



def show_us_index(request, identifier):
    project = Project.objects.filter(identifier=identifier)[0]
    if not project:
        return HttpResponseNotFound('Page not found!')

    us_stories = UserStory.objects.filter(project=project)
    return render(request, 'us_home.html', {
        'title': 'User Stories',
        'us_stories': us_stories,
        'form': UserStoryForm(),
        'project_id': project.identifier
    })


def new_us(request, identifier):
    project = Project.objects.filter(identifier=identifier)[0]
    if not project:
        return HttpResponseNotFound('Page not found!')
    us_stories = UserStory.objects.filter(project=project)
    form = UserStoryForm(data=request.POST)
    if form.is_valid():
        #us = form.save(commit=False)
        #us.project = project
        form.save(project)
        return redirect('/projects/%s/user_stories/' % identifier)
    return render(request, 'us_home.html', {
        'title': 'User Stories',
        'us_stories': us_stories,
        'form': form,
        'project_id': project.identifier
    })