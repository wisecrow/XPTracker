from unittest import skip

from .base import BaseTest


class ProjecValidationTest(BaseTest):

    @skip
    def test_cannot_add_empty_vals(self):
        self.browser.get(self.live_server_url)
        self.browser.find_element_by_id('id_title').send_keys('\n')
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "Project title cannot be empty")

        self.browser.get(self.live_server_url)
        self.browser.find_element_by_id('id_description').send_keys('\n')
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "Project description cannot be empty")

        self.browser.get(self.live_server_url)
        self.browser.find_element_by_id('id_release_date').send_keys('\n')
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "Project release date cannot be empty")

        self.browser.get(self.live_server_url)
        self.browser.find_element_by_id('id_identifier').send_keys('\n')
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "Project identifier cannot be empty")
