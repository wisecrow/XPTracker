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
	project_fields = [
		'title',
		'description',
		'release_date',
		'identifier'
	]

	projects_fields_vals=[
		['My new project1', 'My new project description1', '2016-08-01', 'my-new-project1'],
		['My new project2', 'My new project description2', '2016-08-02', 'my-new-project2'],
		['My new project3', 'My new project description3', '2016-08-03', 'my-new-project3'],
		['My new project4', 'My new project description4', '2016-08-04', 'my-new-project4']
	]
# 	titles = {
# 		'my new project': 'my-new-project',
# 		'my other project ': 'my-other-project',
# 		'&^$%$#(* -)(test 2+++___ #@#$^ ': 'test-2'
# 	}
#
# 	def test_get_url_string(self):
# 		for key, value in ProjectHomePageTest.titles.items():
# 			self.assertEqual(get_url_string(key), value)

	def get_new_projects_request(self, data):
		request = HttpRequest()
		request.method = 'POST'
		request.POST['title'] = data[0]
		request.POST['description'] = data[1]
		request.POST['release_date'] = data[2]
		request.POST['identifier'] = data[3]
		return request


	def test_can_create_and_retrieve_project(self):
		projects = ProjectHomePageTest.projects_fields_vals
		for vals in ProjectHomePageTest.projects_fields_vals:
			p = Project(
				title = vals[0],
				description = vals[1],
				release_date = vals[2] ,
				identifier = vals[3])
			p.save()


		for i, p in enumerate(Project.objects.all(), 0):
			self.assertEqual(p.title, projects[i][0])
			self.assertEqual(p.description, projects[i][1])
			self.assertEqual(p.release_date.strftime('%Y-%m-%d'), projects[i][2])
			self.assertEqual(p.identifier, projects[i][3])



	def test_can_create_project_from_post(self):
		data=ProjectHomePageTest.projects_fields_vals[0]
		show_projects(self.get_new_projects_request(data))

		self.assertEqual(Project.objects.count(), 1)
		p1 = Project.objects.first()
		self.assertEqual(p1.title, data[0])
		self.assertEqual(p1.description, data[1])
		self.assertEqual(p1.release_date.strftime('%Y-%m-%d'), data[2])
		self.assertEqual(p1.identifier, data[3])


	def test_new_project_redirects_to_project_home(self):
		data = ProjectHomePageTest.projects_fields_vals[0]
		response = show_projects(self.get_new_projects_request(data))
		self.assertEqual(response.status_code, 302)
		self.assertEqual(response['location'], '/projects/%s/' % data[3])


	def test_can_retrieve_project_by_identifier(self):
		data = ProjectHomePageTest.projects_fields_vals[0]
		show_projects(self.get_new_projects_request(data))
		p1 = Project.objects.filter(identifier=data[3])
		self.assertEqual(p1[0].title, data[0])



	def test_can_get_html_after_project_creation(self):
		data=ProjectHomePageTest.projects_fields_vals[0]
		show_projects(self.get_new_projects_request(data))
		response=self.client.get('/projects/%s/' % data[3])
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'project.html')
		self.assertContains(response, data[0])


	def test_index_page_has_index_of_projects(self):
		for data in ProjectHomePageTest.projects_fields_vals:
			show_projects(self.get_new_projects_request(data))
		#import pdb; pdb.set_trace()
		response = self.client.get('/projects/')

		for data in ProjectHomePageTest.projects_fields_vals:
			self.assertContains(response, data[0])



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



