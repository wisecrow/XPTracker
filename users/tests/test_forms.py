from django.test import TestCase

from users.models import Developer, FIELDS

from users.forms import NewDeveloperForm, ERROR_MESSAGES

class DeveloperFormTest(TestCase):
    
    def test_form_renders_input(self):
        form = NewDeveloperForm()
        # self.fail(form.as_p())
        self.assertIn('Developers first name"', form.as_p())
        self.assertIn('Developers last name"', form.as_p())
        self.assertIn('Developers email"', form.as_p())
    

    def test_form_validation_empty_input(self):
        form = NewDeveloperForm(data={'firstname': ''})
        self.assertFalse(form.is_valid())
        for field in FIELDS:
            self.assertEqual(
                form.errors[field], [ERROR_MESSAGES.get(field).get('required')]
            )
