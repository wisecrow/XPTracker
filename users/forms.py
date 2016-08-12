from django import forms
from users.models import Developer

ERROR_MESSAGES = {
    'firstname': {'required': 'First name is required!'},
    'lastname': {'required': 'Last name is required!'},
    'email': {'required': 'Email is required!'}
}

FIELDS_IDS = {
    'firstname': 'id_firstname',
    'lastname': 'id_lastname',
    'email': 'id_email'
}


class NewDeveloperForm(forms.ModelForm):
    use_required_attribute = False

    class Meta:

        error_messages = ERROR_MESSAGES
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
                'type': 'email',
                'class': 'form-control'}),
        }
