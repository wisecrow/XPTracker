from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import unittest
from django.test import LiveServerTestCase
from selenium.webdriver.common.keys import Keys

class FirstTimeVisitTest(LiveServerTestCase):

	def setUp(self):
		binary = FirefoxBinary('/usr/bin/firefox')
		self.browser = webdriver.Firefox(firefox_binary=binary)
		# self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()


	def test_can_visit_home_page(self):
		# PM visits project website entering url address http://localhost:8000
		self.browser.get(self.live_server_url)

		# and sees websites titele XP Tracker
		self.assertIn('Projects', self.browser.title )

		# and sees heading 'Projects'
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertEqual(header_text, 'Projects')


	def test_can_enter_project_title_and_redirect_to_projects_home(self):
		self.browser.get(self.live_server_url)
		#self.browser.get('http://localhost:8000')
		# he sees input field and invitation to enter projects title
		inputbox = self.browser.find_element_by_id('id_title')

		self.assertEqual(
			inputbox.get_attribute('placeholder'),
			'Enter a projects title'
		)


		inputbox.send_keys('my new project')
		inputbox.send_keys(Keys.ENTER)

		self.assertRegex(self.browser.current_url, '/projects/my-new-project/$')

		# he does it again
		self.browser.get(self.live_server_url)
		#self.browser.get('http://localhost:8000')


		inputbox = self.browser.find_element_by_id('id_title')
		inputbox.send_keys('my other project')
		inputbox.send_keys(Keys.ENTER)
		self.assertRegex(self.browser.current_url, '/projects/my-other-project/$')


	def test_empty_submited_title_does_nothing(self):
		self.browser.get(self.live_server_url)
		inputbox = self.browser.find_element_by_id('id_title')
		inputbox.send_keys(' ')
		inputbox.send_keys(Keys.ENTER)
		#import time
		#time.sleep(10)
		self.assertEqual('%s/' % self.live_server_url, self.browser.current_url)




