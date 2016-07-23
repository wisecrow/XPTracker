from django.shortcuts import render, redirect
from django.http import HttpResponse
from user_stories.models import UserStory
from project.models import Project
from django.http import  HttpResponseNotFound

def show_us_index(request, identifier):
	project = Project.objects.filter(identifier=identifier)[0]
	if not project:
		return HttpResponseNotFound('Page not found!')
	if request.method=='POST':
		us = UserStory(
			title=request.POST.get('title'),
			estimate_time=request.POST.get('estimate_time'),
			project=project)
		us.save()
		return redirect('/projects/%s/user_stories/' % identifier)

	us_stories = UserStory.objects.filter(project=project)
	return render(request, 'us_home.html', {
		'title': 'User Stories',
		'us_stories': us_stories
	})
