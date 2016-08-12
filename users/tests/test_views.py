from project.tests.base import BaseTest
from django.http import HttpRequest
from users.views import new_developer
from users.forms import NewDeveloperForm, ERROR_MESSAGES
from users.models import Developer, FIELDS

class UsersIndexTest(BaseTest):
    #def test_users_index_renders_html(self):
     #   project = self.create_new_project()
      ## self.assertTemplateUsed(response, 'developers.html')

    def test_show_developer_form(self):
        project = self.create_new_project()
        response = self.client.post('/projects/%s/developers/' % project.identifier)
        self.assertIsInstance(response.context['form'], NewDeveloperForm)
        self.assertContains(response, 'type="text"')
        self.assertContains(response, 'type="email"')

    def test_post_creates_new_dev(self):
        project = self.create_new_project()
        self.client.post('/projects/%s/developers/new/' % project.identifier, data={
            'firstname':'Ttttt',
            'lastname':'Buuuuu',
            'email':'dddd@dfdfd.lt'
        })

        self.assertEqual(Developer.objects.count(), 1)

    def test_validatation_error_sends_bank_to_index(self):
        project = self.create_new_project()
        response = self.client.post('/projects/%s/developers/new/' % project.identifier, data={'firstname': ''})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'developers.html')
        for field in FIELDS:
            expected_error = ERROR_MESSAGES[field]['required']
            self.assertContains(response, expected_error)



