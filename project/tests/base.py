from project.models import Project

from django.test import TestCase

from django.http import HttpRequest

PROJECT_TEST_VALS = {
    'title': 'My new project1',
    'description': 'My new project description1',
    'release_date': '2016-10-01',
    'identifier': 'my-new-procect1'
}

class BaseTest(TestCase):
    project_fields = [
        'title',
        'description',
        'release_date',
        'identifier'
    ]

    projects_fields_vals = [
        ['My new project1', 'My new project description1', '2016-08-01', 'my-new-project1'],
        ['My new project2', 'My new project description2', '2016-08-02', 'my-new-project2'],
        ['My new project3', 'My new project description3', '2016-08-03', 'my-new-project3'],
        ['My new project4', 'My new project description4', '2016-08-04', 'my-new-project4']
    ]

    user_stories_fields = [
        'title',
        'estimate_time'
    ]

    user_stories_vals = [
        ['User story1', 1],
        ['User story2', 2],
        ['User story3', 3],
        ['User story4', 4]

    ]

    def get_new_projects_request(self, data):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['title'] = data[0]
        request.POST['description'] = data[1]
        request.POST['release_date'] = data[2]
        request.POST['identifier'] = data[3]
        return request

    def create_new_project(self):
        project = Project(
            title=PROJECT_TEST_VALS.get('title'),
            description=PROJECT_TEST_VALS.get('description'),
            release_date=PROJECT_TEST_VALS.get('release_date'),
            identifier=PROJECT_TEST_VALS.get('identifier'))
        project.save()
        return project

# class ProjectHomePageTest(BaseTest):

# 	titles = {
# 		'my new project': 'my-new-project',
# 		'my other project ': 'my-other-project',
# 		'&^$%$#(* -)(test 2+++___ #@#$^ ': 'test-2'
# 	}
#
# 	def test_get_url_string(self):
# 		for key, value in ProjectHomePageTest.titles.items():
# 			self.assertEqual(get_url_string(key), value)
#		response = self.client.get('/projects/%s/' % data[3])
# 		for key, value in ProjectHomePageTest.titles.items():
# 			found = resolve('/')
# 			request.method = 'POST'
# 			request.POST['title'] = key
# 			response = show_index(request)
# 			self.assertEqual(response.status_code, 302)
# 			self.assertEqual(response['location'], '/projects/%s/' % ProjectHomePageTest.titles[key])
#
#
# 	def test_empty_post_does_nothing(self):
# 		request = HttpRequest()
# 		request.method = 'POST'
# 		request.POST['title'] = ' '
# 		response = show_index(request)
# 		self.assertContains(response, "Projects")
#
# 	#def test_new_project_page_shows_html(self):
# 	#	response = self.client.get('/projects/my-new-project/')
# 	#	self.assertContains(response, 'my new project')
#
# 	def test_project_can_create_and_retreave(self):
# 		project = Project()
# 		project.title = 'My tdd project'
# 		project.description = 'Testing tdd project and other stuff'
# 		project.release_date = '2016-08-01'
# 		project.active = True
# 		project.date_created = '2016-07-15'
# 		project.save()
# 		self.assertEqual(Project.objects.count(), 1)
#
# 	def test_can_create_new_project_from_post(self):
# 		request = HttpRequest()
# 		request.method = 'POST'
# 		request.POST['title'] = 'popopo'
# 		show_index(request)
# 		response = show_project(request, 'popopo')
# 		self.assertContains(response, "popopo")
#
