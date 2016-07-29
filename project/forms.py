from django import forms

from project.models import Project, PROJECT_FIELDS


ERROR_MESSAGES = {
    'title': {'required': "Project title cannot be empty"},
    'description': {'required': "Project description cannot be empty"},
    'release_date': {'required': "Project release date cannot be empty"},
    'identifier': {'required': "Project identifier cannot be empty"}
}

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = tuple(PROJECT_FIELDS)
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
