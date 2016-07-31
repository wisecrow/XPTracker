from django import forms
from users.models import Developer

class NewDeveloperForm(forms.ModelForm):
    class Meta:
        model = Developer
        fields = ('firstname', 'lastname', 'email')
        widgets = {
            'firstname': forms.fields.TextInput(attrs={
                'placeholder': 'Developers first name',
                'class': 'form-control'}),

            'lastname': forms.fields.TextInput(attrs={
                'placeholder': 'Developers last name',
                'class': 'form-control'}),

            'email': forms.fields.TextInput(attrs={
                'placeholder': 'Developers email',
                'type'  : 'email',
                'class': 'form-control'}),
        }