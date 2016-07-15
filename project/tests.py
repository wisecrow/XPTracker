from django.core.urlresolvers import resolve
from django.test import TestCase
from project.views import show_index, get_url_string
from django.http import HttpRequest
from django.template.loader import render_to_string

class HomePageTest(TestCase):

	def test_root_url_resolves_to_home_page_view(self):
		found = resolve('/')
		self.assertEqual(found.func, show_index)

	def test_home_page_returns_correct_html(self):
		request = HttpRequest()
		response = show_index(request)
		expected_html = render_to_string('home.html', {
			'title':'Projects'
		},
		request=request)
		self.assertEqual(response.content.decode(), expected_html)



class ProjectHomePageTest(TestCase):
	titles = {
		'my new project': 'my-new-project',
		'my other project ': 'my-other-project',
		'&^$%$#(* -)(test 2+++___ #@#$^ ': 'test-2'
	}

	def test_get_url_string(self):
		for key, value in ProjectHomePageTest.titles.items():
			self.assertEqual(get_url_string(key), value)


	def test_new_project_redirects_to_project_home(self):

		request = HttpRequest()

		for key, value in ProjectHomePageTest.titles.items():
			found = resolve('/')
			request.method = 'POST'
			request.POST['title'] = key
			response = show_index(request)
			self.assertEqual(response.status_code, 302)
			self.assertEqual(response['location'], '/projects/%s/' % ProjectHomePageTest.titles[key])


	def test_empty_post_does_nothing(self):
		request = HttpRequest()
		request.method = 'POST'
		request.POST['title'] = ' '
		response = show_index(request)
		self.assertContains(response, "Projects")


