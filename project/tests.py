from django.core.urlresolvers import resolve
from django.test import TestCase
from project.views import show_index
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
		})
		self.assertEqual(response.content.decode(), expected_html)




