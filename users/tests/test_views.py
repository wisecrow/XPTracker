from project.tests.base import BaseTest
from django.http import HttpRequest
from users.views import new_developer
from users.forms import NewDeveloperForm
from users.models import Developer

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



