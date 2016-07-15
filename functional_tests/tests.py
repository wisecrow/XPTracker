from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import unittest

class FirstTimeVisitTest(unittest.TestCase):

	def setUp(self):
		binary = FirefoxBinary('/usr/bin/firefox')
		self.browser = webdriver.Firefox(firefox_binary=binary)
		# self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()


	def test_can_visit_home_page(self):
		# PM visits project website entering url address http://localhost:8000
		self.browser.get('http://localhost:8000')

		# and sees websites titele XP Tracker
		self.assertIn('Projects', self.browser.title )

		# and sees heading 'Projects'
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertEqual(header_text, 'Projects')

		# he sees input field and invitation to enter projects title
		inputbox = self.browser.find_element_by_id('id_title')

		self.assertEqual(
			inputbox.get_attribute('placeholder'),
			'Enter a projects title'
		)

