from django.test import TestCase

from project.forms import ProjectForm, ERROR_MESSAGES


class ProjectFormTest(TestCase):
    
    def test_form_renders_input(self):
        form = ProjectForm()
        # self.fail(form.as_p())
        self.assertIn('Projects title"', form.as_p())
        self.assertIn('Projects description"', form.as_p())
        self.assertIn('Projects release date"', form.as_p())
        self.assertIn('Projects identifier"', form.as_p())

    def test_form_validation_empty_input(self):
        form = ProjectForm(data={'title': ''})
        self.assertFalse(form.is_valid())
        fields = ['title', 'description', 'release_date', 'identifier']
        for field in fields:
            self.assertEqual(
                form.errors[field],
                [ERROR_MESSAGES.get(field).get('required')]
            )

    def test_form_validation_past_release_date(self):
        data = {
            'title': 'Title12',
            'description': 'Desctiptiondfdfd',
            'release_date': '1900-01-01',
            'identifier': 'sdsdsdsww'
        }

        form = ProjectForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['release_date'], [ERROR_MESSAGES['release_date']['only_future']])

