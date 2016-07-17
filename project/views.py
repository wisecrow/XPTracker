from django.shortcuts import render, redirect
from project.models import Project
from django.http import HttpResponse
import re

def show_index(request):
	return redirect('/projects/')


def show_projects(request):

	if request.method == 'POST':
		identifier = request.POST.get('identifier', '')
		p1=Project(
			title=request.POST.get('title', ''),
			description=request.POST.get('description', ''),
			release_date=request.POST.get('release_date', ''),
			identifier=identifier
		)

		p1.save()
		return redirect('/projects/%s/' % identifier)

	projects = Project.objects.all()
	return render(request, 'projects.html',
				  {
					  'title':'Projects',
					  'projects':projects
				  })

def show_project(request, id):
	project = Project.objects.filter(identifier=id)
	if project:
		return render(request, 'project.html', {'project':project[0]})
	return redirect('/projects/')


def get_url_string(title):
	return re.sub(r'[^a-zA-Z0-9]', ' ',  title).strip().replace(' ', '-').lower()