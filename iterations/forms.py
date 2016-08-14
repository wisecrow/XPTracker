from django import forms

from iterations.models import Iteration
from user_stories.models import UserStory
from project.models import Project

DURATION_CHOICES = ((1, 1), (2, 2), (3, 3), (4, 4))


class UserStoryChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return "%s" % obj.title 

class IterationForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        projectid = kwargs.pop('projectid', None)
        super(IterationForm, self).__init__(*args, **kwargs)

        if projectid:
            project = Project(id=projectid)
            self.fields['user_story'].queryset = UserStory.objects.filter(project=project)

    class Meta:
        model = Iteration
        fields = ('title', 'duration', 'user_story')

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

    def save(self, project):
        self.instance.project = project
        return super().save()