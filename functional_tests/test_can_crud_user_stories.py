from .base import BaseTest, projects_fields_vals, \
    user_stories_fields, user_stories_vals


class UserStoriesTest(BaseTest):

    def test_us_link_redirects_to_us_index_page(self):

        self.create_new_projects()
        for vals in projects_fields_vals:
            self.browser.get(
                '%s/projects/%s/' % (self.live_server_url, vals[3])
            )
            self.browser.implicitly_wait(10)
            self.browser.find_element_by_link_text(
                'User stories').click()
            self.assertRegex(
                self.browser.current_url,
                '/projects/%s/user_stories/$' % vals[3]
            )
            header_text = self.browser.find_element_by_tag_name('h1').text
            self.assertEqual(header_text, 'User Stories')

    def test_can_see_us_form(self):
        self. create_new_projects()
        for vals in projects_fields_vals:
            self.browser.get(
                '%s/projects/%s/' % (self.live_server_url, vals[3])
            )
            self.browser.find_element_by_link_text(
                'User stories'
            ).click()

            header2_text = self.browser.find_element_by_tag_name('h2').text
            self.assertEqual(header2_text, 'Create a User Story')

            # form = self.browser.find_element_by_tag_name('form')

            input_title = self.browser.find_element_by_id('id_title')
            title_req = input_title.get_attribute('required')
            self.assertEqual(title_req, 'true')

            self.assertEqual(
                input_title.get_attribute('placeholder'),
                'Story title'
            )

            input_estimate_time = self.browser.find_element_by_id(
                'id_estimate_time'
            )
            estimate_req = input_estimate_time.get_attribute('required')
            self.assertEqual(estimate_req, 'true')

            self.assertEqual(
                input_estimate_time.get_attribute('placeholder'),
                'Story estimate time'
            )

            input_submit = self.browser.find_element_by_id('id_submit')
            self.assertEqual(input_submit.get_attribute('type'), 'submit')

    def test_can_create_new_us(self):
        self.create_new_projects()
        for vals in projects_fields_vals:
            url = '%s/projects/%s/user_stories/' \
                % (self.live_server_url, vals[3])
            # give each us a unique title to distinct from other projects us
            prefix = {'id_title': vals[0]}
            self.browser.implicitly_wait(10)
            self.create_new_model(
                user_stories_fields,
                user_stories_vals,
                url,
                prefix=prefix)
            table = self.browser.find_element_by_id('id_list_user_stories')
            rows = table.find_elements_by_tag_name('tr')
            for us_vals in user_stories_vals:
                us_title = '%s %s' % (us_vals[0], vals[0])
                self.assertIn(us_title, [row.text for row in rows])
