from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import unittest
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.common.keys import Keys
from project.views import show_project
from django.http import HttpRequest


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


user_stories_fields=[
	'id_title',
	'id_estimate_time'
]
user_stories_vals=[
	['User story1', 1],
	['User story2', 2],
	['User story3', 3],
	['User story4', 4]

]


class BaseTest(StaticLiveServerTestCase):
	def setUp(self):
		binary = FirefoxBinary('/usr/bin/firefox')
		self.browser = webdriver.Firefox(firefox_binary=binary)
		#self.browser = webdriver.Firefox()

	# self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def create_new_model(self, fields, vals_vals, url, prefix={}):
		for vals in vals_vals:
			self.browser.get(url)
			for i, val in enumerate(vals, 0):
				val = vals[i]
				prf = prefix.get(fields[i], '')
				if prf:
					val = '%s %s' % (val, prf)
				self.browser.implicitly_wait(3)
				self.browser.find_element_by_id(fields[i]).send_keys(val)

			self.browser.find_element_by_id('id_submit').send_keys(Keys.ENTER)

	def create_new_projects(self):
		self.create_new_model(
			project_id_fields,
			projects_fields_vals,
			self.live_server_url
		)


class FirstTimeHomePageVisitTest(BaseTest):
	# LiveServerTestCase solves test isolation problem, but tests should be lauched by Django testruner - manage.py test

	def test_can_visit_home_page(self):
		# PM visits project website entering url address http://localhost:8000
		self.browser.get(self.live_server_url)

		self.assertRegex(self.browser.current_url, '/projects/$')
		# and sees websites titele XP Tracker
		self.assertIn('Projects', self.browser.title )

		header2_text = self.browser.find_element_by_tag_name('h1').text
		self.assertEqual(header2_text, 'Create a new project')

	def test_can_see_new_project_form(self):
		self.browser.get(self.live_server_url)


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

	def test_layout_and_styling(self):

		self.browser.get(self.live_server_url)
		self.browser.set_window_size(1024, 768)


	#def test_can_create_new_project(self):
	#	self.create_new_projects()
	#
	# 	for vals in projects_fields_vals:
	# 		self.browser.get('%s/projects/%s/' % (self.live_server_url, vals[3]))
	# 		self.assertRegex(self.browser.current_url, '/projects/%s/$' % vals[3])
	# 		id_fields=project_id_fields
	# 		self.assertIn(vals[0], self.browser.title)
	# 		self.assertEqual(self.browser.find_element_by_id(id_fields[0]).text, vals[0])
	# 		self.assertEqual(self.browser.find_element_by_id(id_fields[1]).text, vals[1])
	# 		self.assertEqual(self.browser.find_element_by_id(id_fields[2]).text, vals[2])





	# def test_projects_index_page_has_project_rows(self):
	#	self.create_new_projects()
	#
	# 	self.browser.get(self.live_server_url)
	# 	table = self.browser.find_element_by_id('id_list_projects')
	# 	rows = table.find_elements_by_tag_name('tr')
	# 	for vals in projects_fields_vals:
	# 		self.assertIn(vals[0], [row.text for row in rows])
	# 		alink = self.browser.find_element_by_link_text(vals[0])
	# 		self.assertEqual(alink.text, vals[0])
	#
	# def test_projects_index_links_redirects_to_project_home(self):
	#	self.create_new_projects()
	#
	#
	# 	for vals in projects_fields_vals:
	# 		self.browser.get(self.live_server_url)
	# 		alink = self.browser.find_element_by_link_text(vals[0])
	# 		alink.click()
	# 		heading = self.browser.find_element_by_id('id_title').text
	# 		self.assertEqual(vals[0], heading)


class ProjectHomeTest(BaseTest):


	def test_us_link_redirects_to_us_index_page(self):

		self.create_new_projects()

		for vals in projects_fields_vals:
			self.browser.get('%s/projects/%s/' % (self.live_server_url, vals[3]))
			us_link = self.browser.find_element_by_link_text('User stories').click()
			self.assertRegex(self.browser.current_url, '/projects/%s/user_stories/$' % vals[3])
			header_text = self.browser.find_element_by_tag_name('h1').text
			self.assertEqual(header_text, 'User Stories')

	def test_can_see_us_form(self):
		self. create_new_projects()
		for vals in projects_fields_vals:
			self.browser.get('%s/projects/%s/' % (self.live_server_url, vals[3]))
			us_link = self.browser.find_element_by_link_text('User stories').click()

			header2_text = self.browser.find_element_by_tag_name('h2').text
			self.assertEqual(header2_text, 'Create a User Story')

			form = self.browser.find_element_by_tag_name('form')

			input_title = self.browser.find_element_by_id('id_title')
			self.assertAlmostEqual(
				input_title.location['x'] + input_title.size['width'] / 2,
				423,
				delta=5
			)
			title_req = input_title.get_attribute('required')
			self.assertEqual(title_req, 'true')

			self.assertEqual(
				input_title.get_attribute('placeholder'),
				'Enter User Story title'
			)

			input_estimate_time = self.browser.find_element_by_id('id_estimate_time')
			estimate_req = input_estimate_time.get_attribute('required')
			self.assertEqual(estimate_req, 'true')

			self.assertEqual(
				input_estimate_time.get_attribute('placeholder'),
				'Enter User Stories estimate time'
			)

			input_submit = self.browser.find_element_by_id('id_submit')
			self.assertEqual(input_submit.get_attribute('value'), 'Submit')

	def test_can_create_new_us(self):
		self.create_new_projects()
		for vals in projects_fields_vals:
			url =  '%s/projects/%s/user_stories/' %  (self.live_server_url, vals[3])
			# give each us a unique title to distinct from other projects us
			prefix = {'id_title': vals[0]}
			self.create_new_model(user_stories_fields, user_stories_vals, url, prefix=prefix)
			table = self.browser.find_element_by_id('id_list_user_stories')
			rows = table.find_elements_by_tag_name('tr')
			for us_vals in user_stories_vals:
				us_title = '%s %s' % (us_vals[0], vals[0])
				self.assertIn(us_title, [row.text for row in rows])
















