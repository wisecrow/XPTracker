from project.tests.base import BaseTest
from tasks.forms import TaskForm

class TaskCreateTest(BaseTest):

    def test_tasks_url_resolves_correctly(self):
        project, iteration = self.create_new_iteration()
        response = self.go_tasks_home(project)
        self.assertEqual(response.status_code, 200)

    def test_template_uses_form(self):
        project, iteration = self.create_new_iteration()
        response = self.go_tasks_home(project)
        self.assertIsInstance(response.context['form'], TaskForm)

