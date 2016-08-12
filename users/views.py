from django.shortcuts import render, redirect
from users.forms import NewDeveloperForm
from project.models import Project
from users.models import Developer

def show_index(request, id):
    projects = Project.objects.filter(identifier=id)
    form = NewDeveloperForm()
    developers = Developer.objects.all()
    return render(request, 'developers.html', {
        'title':'Developers',
        'form' : form,
        'project_id': projects[0].identifier,
        'developers':developers
    })

def new_developer(request, id):
    projects = Project.objects.filter(identifier=id)
    form = NewDeveloperForm(data=request.POST)
    developers = Developer.objects.all()
    if form.is_valid():
        form.save()
        return redirect('/projects/%s/developers/' % projects[0].identifier)
    return render(request, 'developers.html', {
        'form': form,
        'project_id': projects[0].identifier,
        'title': 'Developers',
        'developers': developers})
