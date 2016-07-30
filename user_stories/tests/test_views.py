from django.http import HttpRequest

from user_stories.views import show_us_index, new_us

from user_stories.forms import UserStoryForm

from .base import get_new_us_request

from project.tests.base import BaseTest

class IndexTest(BaseTest):

    def test_us_index_resolves_correctly(self):
        project = self.create_new_project()
        response = self.client.get('/projects/%s/user_stories/' % project.identifier)
        self.assertEqual(response.status_code, 200)

    def test_index_uses_home_template(self):
        project = self.create_new_project()
        response = self.client.get('/projects/%s/user_stories/' % project.identifier)
        self.assertTemplateUsed(response, 'us_home.html')

class CreatNewTest(BaseTest):

    def test_new_us_resolves_correctly(self):
        project = self.create_new_project()
        response = self.client.get('/projects/%s/user_stories/' % project.identifier)
        request = get_new_us_request()
        response = new_us(request, project.identifier)
        self.assertEqual(response.status_code, 302) 

    def test_redirects_after_us_post(self):
        project = self.create_new_project()
        response = self.client.get('/projects/%s/user_stories/' % project.identifier)
        request = get_new_us_request()
        response = new_us(request, project.identifier)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/projects/%s/user_stories/' % project.identifier)

    def test_template_uses_form(self):
        project = self.create_new_project()
        response = self.client.get('/projects/%s/user_stories/' % project.identifier)
        self.assertIsInstance(response.context['form'], UserStoryForm)

 #  def test_us_shows
