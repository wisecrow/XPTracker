from .base import BaseTest
from XPTracker.base import PROJECT_TITLE, PROJECT_DESCR, PROJECT_RELEASE_DATE, PROJECT_ID, US_FIELDS_IDS


class UserStoriesTest(BaseTest):

    def test_us_link_redirects_to_us_index_page(self):

        project = self.create_new_project()
        self.browser.get(
                '%s/projects/%s/' % (self.live_server_url, project[PROJECT_ID])
        )

        self.browser.implicitly_wait(5)
        self.browser.find_element_by_link_text(
            'User stories').click()
        self.assertRegex(
        self.browser.current_url,
            '/projects/%s/user_stories/$' % project[PROJECT_ID]
        )
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertEqual(header_text, 'User Stories')

    def test_can_see_us_form(self):
        project = self. create_new_project()
  
        self.browser.implicitly_wait(5)
        self.browser.get(
            '%s/projects/%s/' % (self.live_server_url, project[PROJECT_ID])
        )
        self.browser.find_element_by_link_text(
                'User stories'
            ).click()

        header2_text = self.browser.find_element_by_tag_name('h2').text
        self.assertEqual(header2_text, 'Create a User Story')

            # form = self.browser.find_element_by_tag_name('form')

        input_title = self.browser.find_element_by_id('id_title')
           

        self.assertEqual(
                input_title.get_attribute('placeholder'),
                'Story title'
        )

        input_estimate_time = self.browser.find_element_by_id(
                'id_estimate_time'
        )
            

        self.assertEqual(
            input_estimate_time.get_attribute('placeholder'),
            'Story estimate time'
        )

        input_submit = self.browser.find_element_by_id('id_submit')
        self.assertEqual(input_submit.get_attribute('type'), 'submit')

    def test_can_create_new_us(self):
        project = self.create_new_project()
        url = '%s/projects/%s/user_stories/' \
            % (self.live_server_url, project[PROJECT_ID])
    
           #prefix = {'id_title': vals[0]}
        self.browser.implicitly_wait(10)
        us = self.create_new_us(project)
        table = self.browser.find_element_by_id('id_list_user_stories')
        rows = table.find_elements_by_tag_name('tr')
        us_title = us['title']
        self.assertIn(us_title, [row.text for row in rows])

 
