from django import forms

from iterations.models import Iteration
from user_stories.models import UserStory
from project.models import Project

DURATION_CHOICES = ((1, 1), (2, 2), (3, 3), (4, 4))


class UserStoryChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return "%s" % obj.title 

class IterationForm(forms.Form):

    def __init__(self, *args, **kwargs):
        #import pdb; pdb.set_trace()
        projectid = kwargs.pop('projectid', None)
        super(IterationForm, self).__init__(*args, **kwargs)

        if projectid:
            project = Project(id=projectid)
            self.fields['user_story'].queryset = UserStory.objects.filter(project=project)

    #lass Meta:
        #fields = ('title', 'duration')
        #model = Iteration
    title = forms.CharField(
        label='Title',
        widget=forms.fields.TextInput(
            attrs={
                'class': 'form-control'
            }))
    duration = forms.ChoiceField(
        choices=DURATION_CHOICES,
        widget=forms.fields.Select(
            attrs={
                'class': 'form-control'
            }))

    user_story = UserStoryChoiceField(
        queryset=UserStory.objects.all(),
        widget=forms.fields.Select(
            attrs={
                'class': 'form-control' 
            }))