from project.tests.base import BaseTest
from iterations.forms import IterationForm
from iterations.models import Iteration

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

    def test_post_creates_iteration(self):
        self.get_iteration_post_response()
        self.assertEqual(Iteration.objects.count(), 1)

    def test_redirects_after_post(self):
        response = self.get_iteration_post_response()
        self.assertEqual(response.status_code, 302)

    def get_iteration_post_response(self):
        project = self.create_new_project()
        us = self.create_new_us(project)
        url = '/projects/%s/iterations/new/' % project.identifier
        data = {
            'title': 'Test title',
            'duration': 3,
            'user_story': us.id,
        }
        return self.client.post(url, data)

    def test_index_has_list_of_iterations(self):
        project = self.create_new_project()
        us = self.create_new_us(project)
        iteration = Iteration(
            title='Title',
            duration=4,
            user_story=us,
            project=project)
        iteration.save()

        url = '/projects/%s/iterations/' % project.identifier
        response = self.client.get(url)
        self.assertContains(response, iteration.title)

