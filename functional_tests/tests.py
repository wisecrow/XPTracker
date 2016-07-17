from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import unittest
from django.test import LiveServerTestCase
from selenium.webdriver.common.keys import Keys

class FirstTimeHomePageVisitTest(LiveServerTestCase):
	# LiveServerTestCase solves test isolation problem, but tests should be lauched by Django testruner - manage.py test

	def setUp(self):
		binary = FirefoxBinary('/usr/bin/firefox')
		self.browser = webdriver.Firefox(firefox_binary=binary)
		# self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()


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
		self.browser.get(self.live_server_url)

		self.browser.find_element_by_id('id_title').send_keys('My new project')

		self.browser.find_element_by_id('id_description').send_keys('My new project description')

		self.browser.find_element_by_id('id_release_date').send_keys('2016-08-01')

		self.browser.find_element_by_id('id_identifier').send_keys('my-new-project')

		self.browser.find_element_by_id('id_submit').send_keys(Keys.ENTER)

		#self.browser.get(self.live_server_url)

		self.assertRegex(self.browser.current_url, '/projects/my-new-project/$')

		self.assertIn('My new project', self.browser.title)

		# and sees heading 'Projects'
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertEqual(header_text, 'My new project')

	# 	# he sees input field and invitation to enter projects title
	# 	inputbox = self.browser.find_element_by_id('id_title')
	#
	# 	self.assertEqual(
	# 		inputbox.get_attribute('placeholder'),
	# 		'Enter a projects title'
	# 	)
	#
	#
	# 	inputbox.send_keys('my new project')
	# 	inputbox.send_keys(Keys.ENTER)
	#
	# 	self.assertRegex(self.browser.current_url, '/projects/my-new-project/$')
	#
	# 	# he does it again
	# 	self.browser.get(self.live_server_url)
	# 	#self.browser.get('http://localhost:8000')
	#
	#
	# 	inputbox = self.browser.find_element_by_id('id_title')
	# 	inputbox.send_keys('my other project')
	# 	inputbox.send_keys(Keys.ENTER)
	# 	self.assertRegex(self.browser.current_url, '/projects/my-other-project/$')
	#
	# 	# and sees page title New Project
	# 	self.assertIn('New Project', self.browser.title)
	#
	# 	# and sees heading 'New Project'
	# 	header_text = self.browser.find_element_by_tag_name('h1').text
	# 	self.assertEqual(header_text, 'New Project')
	#
	# 	inputbox = self.browser.find_element_by_id('id_title')
	# 	value = inputbox.get_attribute('value')
	# 	self.assertEqual(value, 'my other project')
	#
	#
	# def test_empty_submited_title_does_nothing(self):
	# 	self.browser.get(self.live_server_url)
	# 	inputbox = self.browser.find_element_by_id('id_title')
	# 	inputbox.send_keys(' ')
	# 	inputbox.send_keys(Keys.ENTER)
	# 	#import time
	# 	#time.sleep(10)
	# 	self.assertEqual('%s/' % self.live_server_url, self.browser.current_url)
	#






