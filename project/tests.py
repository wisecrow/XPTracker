from django.core.urlresolvers import resolve
from django.test import TestCase
from project.views import show_index, get_url_string, show_project, show_projects
from django.http import HttpRequest
from django.template.loader import render_to_string
from project.models import Project

class HomePageTest(TestCase):

	def test_root_url_resolves_to_projects_home_page(self):
		response = self.client.get('/')
		self.assertEqual(response.status_code, 302)
		self.assertEqual(response['location'], '/projects/')

		#self.assertEqual(found.func, show_index)

	def test_projects_home_page_returns_correct_html(self):
		request = HttpRequest()
		response = self.client.get('/projects/')
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Projects')

class ProjectHomePageTest(TestCase):
# 	titles = {
# 		'my new project': 'my-new-project',
# 		'my other project ': 'my-other-project',
# 		'&^$%$#(* -)(test 2+++___ #@#$^ ': 'test-2'
# 	}
#
# 	def test_get_url_string(self):
# 		for key, value in ProjectHomePageTest.titles.items():
# 			self.assertEqual(get_url_string(key), value)

	def get_new_projects_request(self):
		request = HttpRequest()
		request.method = 'POST'
		request.POST['title'] = 'New project12'
		request.POST['description'] = 'My new description'
		request.POST['release_date'] = '2016-09-23'
		request.POST['identifier'] = 'new-project12'
		return request


	def test_can_create_and_retrieve_project(self):
		p1 = Project(
			title='New project1',
			description='Description1',
			release_date='2016-08-22',
			identifier='my-project1')
		p1.save()

		p2 = Project(
			title='New project2',
			description='Description2',
			release_date='2016-08-24',
			identifier='my-project2')
		p2.save()

		all_projects = Project.objects.all()
		p1=all_projects[0]
		p2 = all_projects[1]

		self.assertEqual(p1.title, 'New project1')
		self.assertEqual(p1.description, 'Description1')
		self.assertEqual(p1.release_date.strftime('%Y-%m-%d'), '2016-08-22')
		self.assertEqual(p1.identifier, 'my-project1')

		self.assertEqual(p2.title, 'New project2')
		self.assertEqual(p2.description, 'Description2')
		self.assertEqual(p2.release_date.strftime('%Y-%m-%d'), '2016-08-24')
		self.assertEqual(p2.identifier, 'my-project2')

	def test_can_create_project_from_post(self):

		show_projects(self.get_new_projects_request())

		self.assertEqual(Project.objects.count(), 1)
		p1 = Project.objects.first()
		self.assertEqual(p1.title, 'New project12')
		self.assertEqual(p1.description, 'My new description')
		self.assertEqual(p1.release_date.strftime('%Y-%m-%d'), '2016-09-23')
		self.assertEqual(p1.identifier, 'new-project12')


	def test_new_project_redirects_to_project_home(self):
		response = show_projects(self.get_new_projects_request())
		self.assertEqual(response.status_code, 302)
		self.assertEqual(response['location'], '/projects/new-project12/')


	def test_can_retrieve_project_by_identifier(self):
		show_projects(self.get_new_projects_request())
		p1 = Project.objects.filter(identifier='new-project12')
		self.assertEqual(p1[0].title, 'New project12')



	def test_can_get_html_after_project_creation(self):
		show_projects(self.get_new_projects_request())
		response=self.client.get('/projects/new-project12/')
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'project.html')
		self.assertContains(response, 'New project12')



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



