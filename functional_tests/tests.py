from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import unittest
from django.test import LiveServerTestCase
from selenium.webdriver.common.keys import Keys
from project.views import show_project
from django.http import HttpRequest

class FirstTimeHomePageVisitTest(LiveServerTestCase):
	# LiveServerTestCase solves test isolation problem, but tests should be lauched by Django testruner - manage.py test
	project_id_fields=[
		'id_title',
		'id_description',
		'id_release_date',
		'id_identifier'
		]

	projects_fields_vals=[
		['My new project1', 'My new project description1', '2016-08-01', 'my-new-project1'],
		['My new project2', 'My new project description2', '2016-08-02', 'my-new-project2'],
		['My new project3', 'My new project description3', '2016-08-03', 'my-new-project3'],
		['My new project4', 'My new project description4', '2016-08-04', 'my-new-project4']
	]

	def setUp(self):
		#binary = FirefoxBinary('/usr/bin/firefox45')
		#self.browser = webdriver.Firefox(firefox_binary=binary)
		self.browser = webdriver.Firefox()
		# self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def create_new_projects(self, fields, vals_vals):

		for vals in vals_vals:
			self.browser.get(self.live_server_url)
			for i, val in enumerate(vals, 0):
				self.browser.find_element_by_id(fields[i]).send_keys(vals[i])
			self.browser.find_element_by_id('id_submit').send_keys(Keys.ENTER)



	def test_can_visit_home_page(self):
		# PM visits project website entering url address http://localhost:8000
		self.browser.get(self.live_server_url)

		self.assertRegex(self.browser.current_url, '/projects/$')
		# and sees websites titele XP Tracker
		self.assertIn('Projects', self.browser.title )

		# and sees heading 'Projects'
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertEqual(header_text, 'Projects')

	def test_can_see_new_project_form(self):
		self.browser.get(self.live_server_url)

		header2_text = self.browser.find_element_by_tag_name('h2').text
		self.assertEqual(header2_text, 'Create a new project')

		form = self.browser.find_element_by_tag_name('form')

		input_title = self.browser.find_element_by_id('id_title')
		title_req = input_title.get_attribute('required')
		self.assertEqual(title_req, 'true')

		self.assertEqual(
			input_title.get_attribute('placeholder'),
			 		'Enter a projects title'
			 	)

		input_description = self.browser.find_element_by_id('id_description')

		desc_req = input_description.get_attribute('required')
		self.assertEqual(desc_req, 'true')

		self.assertEqual(
			input_description.get_attribute('placeholder'),
			'Enter a projects description'
		)

		input_release_date = self.browser.find_element_by_id('id_release_date')
		rel_date_req = input_release_date.get_attribute('required')
		self.assertEqual(rel_date_req, 'true')

		self.assertEqual(
			input_release_date.get_attribute('placeholder'),
			'Enter a projects release date'
		)

		input_identifier = self.browser.find_element_by_id('id_identifier')
		ident_req = input_identifier.get_attribute('required')
		self.assertEqual(ident_req, 'true')
		self.assertEqual(
			input_identifier.get_attribute('placeholder'),
			'Enter a projects identifier'
		)

		input_submit = self.browser.find_element_by_id('id_submit')
		self.assertEqual(input_submit.get_attribute('value'), 'Submit')

	def test_can_create_new_project(self):
		self.create_new_projects(
			FirstTimeHomePageVisitTest.project_id_fields,
			FirstTimeHomePageVisitTest.projects_fields_vals

		)

		for i, vals in enumerate(FirstTimeHomePageVisitTest.projects_fields_vals, 0):
			self.browser.get('%s/projects/%s/' % (self.live_server_url, vals[3]))
			self.assertRegex(self.browser.current_url, '/projects/%s/$' % vals[3])
			id_fields=FirstTimeHomePageVisitTest.project_id_fields
			self.assertIn(vals[0], self.browser.title)
			self.assertEqual(self.browser.find_element_by_id(id_fields[0]).text, vals[0])
			self.assertEqual(self.browser.find_element_by_id(id_fields[1]).text, vals[1])
			self.assertEqual(self.browser.find_element_by_id(id_fields[2]).text, vals[2])





	def test_projects_index_page_has_project_rows(self):
		self.create_new_projects(
			FirstTimeHomePageVisitTest.project_id_fields,
			FirstTimeHomePageVisitTest.projects_fields_vals
		)

		self.browser.get(self.live_server_url)
		table = self.browser.find_element_by_id('id_list_projects')
		rows = table.find_elements_by_tag_name('tr')
		for vals in FirstTimeHomePageVisitTest.projects_fields_vals:
			self.assertIn(vals[0], [row.text for row in rows])
			alink = self.browser.find_element_by_link_text(vals[0])
			self.assertEqual(alink.text, vals[0])

	def test_projects_index_links_redirects_to_project_home(self):
		self.create_new_projects(
			FirstTimeHomePageVisitTest.project_id_fields,
			FirstTimeHomePageVisitTest.projects_fields_vals
		)


		for vals in FirstTimeHomePageVisitTest.projects_fields_vals:
			self.browser.get(self.live_server_url)
			alink = self.browser.find_element_by_link_text(vals[0])
			alink.click()
			heading = self.browser.find_element_by_id('id_title').text
			self.assertEqual(vals[0], heading)










