from django import forms

from project.models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('title', 'description', 'release_date', 'identifier')
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

        error_messages = {
            'title': {'required': "Project title cannot be empty"},
            'description': {'required': "Project description cannot be empty"},
            'release_date': {'required': "Project release date cannot be empty"},
            'identifier': {'required': "Project identifier cannot be empty"}
        }