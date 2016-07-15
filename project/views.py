from django.shortcuts import render, redirect
from django.http import HttpResponse
import re

def show_index(request):
	if request.method == 'POST':
		title = request.POST['title'].strip()
		if title:
			project_url = get_url_string(request.POST['title'])
			return redirect('/projects/%s/' % project_url)
	return render(request, 'home.html', {
	'title': 'Projects'
	})

def show_project(request, title):
	return HttpResponse()

def get_url_string(title):
	return re.sub(r'[^a-zA-Z0-9]', ' ',  title).strip().replace(' ', '-')