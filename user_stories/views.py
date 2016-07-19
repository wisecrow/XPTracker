from django.shortcuts import render
from django.http import HttpResponse

def show_us_index(request, title, aa):
	return render(request, 'us_home.html', {
		'title':'User Stories'
	})
