from unittest import skip

from django.template.loader import render_to_string

from django.http import HttpRequest

from project.models import Project, PROJECT_FIELDS

from project.forms import ProjectForm, ERROR_MESSAGES

from project.views import new_project, show_projects

from .base import BaseTest


class ProjectViewsTest(BaseTest):

    def test_root_url_resolves_to_projects_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/projects/')

    def test_projects_home_page_returns_correct_html(self):
        # request = HttpRequest()
        response = self.client.get('/projects/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Projects')

    def test_new_project_redirects_to_project_home(self):
        data = BaseTest.projects_fields_vals[0]
        response = new_project(self.get_new_projects_request(data))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/projects/%s/' % data[3])

    def test_can_retrieve_project_by_identifier(self):
        data = BaseTest.projects_fields_vals[0]
        new_project(self.get_new_projects_request(data))
        p1 = Project.objects.filter(identifier=data[3])
        self.assertEqual(p1[0].title, data[0])

    def test_can_get_html_after_project_creation(self):
        data = BaseTest.projects_fields_vals[0]
        new_project(self.get_new_projects_request(data))
        response = self.client.get('/projects/%s/' % data[3])
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'project.html')
        self.assertContains(response, data[0])

    def test_index_page_has_index_of_projects(self):
        for data in BaseTest.projects_fields_vals:
            new_project(self.get_new_projects_request(data))
            response = self.client.get('/projects/')

        for data in BaseTest.projects_fields_vals:
            self.assertContains(response, data[0])

    def test_project_home_page_uses_form(self):
        response = self.client.get('/projects/')
        self.assertIsInstance(response.context['form'], ProjectForm)

    def test_validatation_error_sends_bank_to_index(self):
        response = self.client.post('/projects/new/', data={'title': ''})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'projects.html')

        for pr_field in PROJECT_FIELDS:
            expected_error = ERROR_MESSAGES[pr_field]['required']
            self.assertContains(response, expected_error)
