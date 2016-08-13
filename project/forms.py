from datetime import date

from django import forms

from project.models import Project
from XPTracker.base import BaseProjectModel


ERROR_MESSAGES = {
    'title': {'required': "Project title cannot be empty"},
    'description': {'required': "Project description cannot be empty"},
    'release_date': {
        'required': "Project release date cannot be empty", 
        'only_future': 'Projects release date should be in the future!'},
    'identifier': {'required': "Project identifier cannot be empty"}
}

class ProjectForm(forms.ModelForm):

    # override django 1.10 added feature to disable html validation
    use_required_attribute = False

    class Meta:
        model = Project
        fields = ('title', 'description', 'release_date', 'identifier')
        validators = []
        widgets = {
            'title': forms.fields.TextInput(attrs={
                'placeholder': 'Projects title',
                'class': 'form-control'}),

            'description': forms.fields.TextInput(attrs={
                'placeholder': 'Projects description',
                'class': 'form-control'}),

            'release_date': forms.fields.DateInput(attrs={
                'placeholder': 'Projects release date',
                'class': 'form-control'}),

            'identifier': forms.fields.TextInput(attrs={
                'placeholder': 'Projects identifier',
                'class': 'form-control'})
        }

        error_messages = ERROR_MESSAGES


    def clean_release_date(self):
        """Validate release date.
        Allow only future dates."""

        data = self.cleaned_data['release_date']
        today = date.today()
        if today >= data:
            raise forms.ValidationError(
                ERROR_MESSAGES['release_date']['only_future'])
        return data

