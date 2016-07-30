from django.shortcuts import render

def show_index(request, identifier):
    return render(request, 'developers.html', {
        'title':'Developers'
    })
# Create your views here.
