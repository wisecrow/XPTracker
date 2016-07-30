from project.tests.base import BaseTest

class UsersIndexTest(BaseTest):
    def test_users_index_renders_html(self):
        project = self.create_new_project()
        response = self.client.get('/projects/%s/developers/' % project.identifier)
        self.assertTemplateUsed(response, 'developers.html')

