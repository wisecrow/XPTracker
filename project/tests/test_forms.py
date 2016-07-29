from django.test import TestCase

from project.forms import ProjectForm


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
        self.assertEqual(
            form.errors['title'],
            ["Project title cannot be empty"]
        )
        self.assertEqual(
            form.errors['description'],
            ["Project description cannot be empty"]
        )
        self.assertEqual(
            form.errors['release_date'],
            ["Project release date cannot be empty"]
        )
        self.assertEqual(
            form.errors['identifier'],
            ["Project identifier cannot be empty"]
        )
