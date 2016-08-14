from project.tests.base import BaseTest
from iterations.forms import IterationForm

class IterationCreateTest(BaseTest):

    def test_iterations_index_resolves_correctly(self):
        project = self.create_new_project()
        us = self.create_new_us(project)
        response = self.go_to_iteration_home(project)
        self.assertEqual(response.status_code, 200)

    def test_index_uses_home_template(self):
        project = self.create_new_project()
        us = self.create_new_us(project)
        response = self.go_to_iteration_home(project)
        self.assertTemplateUsed(response, 'iterations.html')

    def test_template_uses_form(self):
        project = self.create_new_project()
        us = self.create_new_us(project)
        response = self.go_to_iteration_home(project)
        self.assertIsInstance(response.context['form'], IterationForm)
