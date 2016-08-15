from django import forms
from tasks.models import Task

FIELDS = ('title', 'description', 'estimate_time', 'developer', 'iteration')
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = FIELDS