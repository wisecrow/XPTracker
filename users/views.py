from django.shortcuts import render
from users.forms import NewDeveloperForm

def show_index(request, identifier):
    form = NewDeveloperForm()
    return render(request, 'developers.html', {
        'title':'Developers',
        'form' : form,
    })

def new_developer(request, identifier):
    pass;
