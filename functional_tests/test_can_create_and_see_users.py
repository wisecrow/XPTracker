from functional_tests.base import BaseTest, projects_fields_vals

class ProjectPageTest(BaseTest):

    def test_developers_index_url_is_correct(self):
        self.create_new_projects()
        for vals in projects_fields_vals:
            self.browser.get(self.live_server_url)
            self.browser.find_element_by_link_text(vals[0]).click()
            self.browser.implicitly_wait(10)
            alink = self.browser.find_element_by_link_text('Developers').click()
            cur_url = self.browser.current_url
            self.assertRegex(cur_url, '/projects/.+/developers/')



    def test_developers_index_shows_form(self):
        self.create_new_projects()
        for vals in projects_fields_vals:
            self.browser.get(self.live_server_url)
            self.browser.find_element_by_link_text(vals[0]).click()
            self.browser.implicitly_wait(10)
            alink = self.browser.find_element_by_link_text('Developers').click()
            firstname_input = self.browser.find_element_by_id('id_firstname')
            lastname_input = self.browser.find_element_by_id('id_lastname')
            email_input = self.browser.find_element_by_id('id_email')

            self.assertEqual(
                firstname_input.get_attribute('placeholder'),
                'Developers first name'
            )

            self.assertEqual(
                lastname_input.get_attribute('placeholder'),
                'Developers last name'
            )

            self.assertEqual(
                email_input.get_attribute('placeholder'),
                'Developers email'
            )





