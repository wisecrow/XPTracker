from django.test import TestCase

from user_stories.forms import UserStoryForm, ERROR_MESSAGES

from user_stories.models import USER_STORY_FIELDS


class UserStoryFormTest(TestCase):
    
    def test_form_renders_input(self):
        form = UserStoryForm()
        # self.fail(form.as_p())
        self.assertIn('Story title"', form.as_p())
        self.assertIn('Story estimate time', form.as_p())

    def test_form_validation_empty_input(self):
        form = UserStoryForm(data={'title': ''})
        self.assertFalse(form.is_valid())
        for field in USER_STORY_FIELDS:
            self.assertEqual(
                form.errors[field],
                [ERROR_MESSAGES.get(field).get('required')]
            )
