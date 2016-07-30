from django import forms

from user_stories.models import UserStory, USER_STORY_FIELDS


ERROR_MESSAGES = {
    'title': {'required': "User story title cannot be empty"},
    'estimate_time': {'required': "Estimate time cannot be empty"}
}

class UserStoryForm(forms.ModelForm):

    

    class Meta:
        model = UserStory
        fields = ('title', 'estimate_time')
        widgets = {
            'title': forms.fields.TextInput(attrs={
                'placeholder': 'Story title',
                'class': 'form-control'}),

            'estimate_time': forms.fields.TextInput(attrs={
                'placeholder': 'Story estimate time',
                'class': 'form-control'}),
        }
        error_messages = ERROR_MESSAGES

    def save(self, project):
        self.instance.project = project
        return super().save()
