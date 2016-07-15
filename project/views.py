from django.shortcuts import render, redirect
from django.http import HttpResponse

def show_index(request):
	if request.method == 'POST':
		return redirect('/projects/my-new-project/')
	return render(request, 'home.html', {
	'title': 'Projects'
	})

def show_project(request):
	return HttpResponse()
