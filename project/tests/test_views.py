from unittest import skip

from django.template.loader import render_to_string

from django.http import HttpRequest

from project.models import Project, FIELDS

from project.forms import ProjectForm, ERROR_MESSAGES

from project.views import new_project, show_projects

from .base import BaseTest

from XPTracker.base import PROJECT_TITLE, PROJECT_DESCR, PROJECT_RELEASE_DATE, PROJECT_ID

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
        data={'title':'Title23', 'description':'Desc dfdfd', 'release_date': '2018-02-01', 'identifier': 'ooo'}
        response = self.client.post('/projects/new/', data=data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/projects/%s/' % data['identifier'])

    def test_can_retrieve_project_by_identifier(self):
        project = self.create_new_project()
        projects = Project.objects.filter(identifier=project.identifier)
        self.assertEqual(projects[0].title, project.title)

    def test_can_get_html_after_project_creation(self):
        project = self.create_new_project()
        response = self.go_to_project_home(project)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'project.html')
        self.assertContains(response, project.title)

    def test_index_page_has_index_of_projects(self):
        project = self.create_new_project()
        response = self.go_to_project_home(project)
        self.assertContains(response, project.title)

    def test_project_home_page_uses_form(self):
        response = self.client.get('/projects/')
        self.assertIsInstance(response.context['form'], ProjectForm)

    def test_validatation_error_sends_bank_to_index(self):
        response = self.client.post('/projects/new/', data={'title': ''})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'projects.html')
        for pr_field in FIELDS:
            expected_error = ERROR_MESSAGES[pr_field]['required']
            self.assertContains(response, expected_error)
