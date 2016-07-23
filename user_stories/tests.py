from django.test import TestCase
from django.http import HttpRequest
from project.tests import BaseTest
from project.views import show_projects
from user_stories.views import show_us_index
from project.models import Project
from user_stories.models import UserStory

class UserStoriesIndexTest(BaseTest):

	def test_us_index_resolves_correctly(self):
		for data in BaseTest.projects_fields_vals:
			show_projects(self.get_new_projects_request(data))
			response = self.client.get('/projects/%s/user_stories/' % data[3])
			self.assertEqual(response.status_code, 200)
			self.assertTemplateUsed(response, 'us_home.html')
			self.assertContains(response, 'User Stories')


	def test_can_create_and_retrieve_us(self):
		p = Project(
				title='Naujasss',
				description='Naujo aprasymas',
				release_date='2016-09-22',
				identifier='naujassss')
		p.save()

		us=UserStory(
			title = 'Nauja us',
			estimate_time = 10,
			project = p

		)

		us.save()
		self.assertEqual(UserStory.objects.count(), 1)
		u1 = UserStory.objects.all()[0]
		self.assertEqual(u1.title, 'Nauja us')
		self.assertEqual(u1.project.title, 'Naujasss')

	def test_can_create_and_retrieve_us_from_project_context(self):
		us_vals = {'title': 'US blabla bla', 'estimate_time':2}
		us_iterate = 3
		for data in BaseTest.projects_fields_vals:
			show_projects(self.get_new_projects_request(data))
			for i, iter in enumerate(range(us_iterate), 0):
				self.client.get('/projects/%s/user_stories/' % data[3])
				request = HttpRequest()
				request.method = 'POST'
				request.POST['title'] = "%s %s" % (us_vals['title'], i)
				request.POST['estimate_time'] = us_vals['estimate_time']
				show_us_index(request, data[3])
				us_response = self.client.get('/projects/%s/user_stories/' % data[3])
				self.assertContains(us_response, "%s %s" % (us_vals['title'], i) )
				prev_us = i -0
				if prev_us > 0:
					for prev in range(prev_us):
						self.assertContains(us_response, "%s %s" % (us_vals['title'], prev))


	def test_redirects_after_us_post(self):
		request = HttpRequest()
		request.method='POST'
		request.POST['title'] = 'tttt'
		request.POST['release_date']='2016-08-09'
		request.POST['identifier'] = 'tttt'
		request.POST['description'] = 'dddddddddddddddddddddd'
		show_projects(request)
		self.client.get('/projects/tttt/user_stories/')
		request = HttpRequest()
		request.method = 'POST'
		request.POST['title'] = 'ususus'
		request.POST['estimate_time']=2
		response = show_us_index(request, 'tttt')
		self.assertEqual(response.status_code, 302)
		self.assertEqual(response['location'], '/projects/tttt/user_stories/')


