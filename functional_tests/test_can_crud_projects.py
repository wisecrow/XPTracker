from unittest import skip

from selenium.webdriver.common.keys import Keys

from project.forms import ERROR_MESSAGES

from functional_tests.base import BaseTest

from XPTracker.base import PROJECT_TITLE, PROJECT_DESCR, PROJECT_RELEASE_DATE, PROJECT_ID, BaseProjectModel

class FirstTimeHomePageVisitTest(BaseTest):
    """LiveServerTestCase solves test isolation problem.
    But tests should be lauched by Django testruner - manage.py test.
    """

    def test_can_visit_home_page(self):
        # PM visits project website entering url address http://localhost:8000
        self.browser.get(self.live_server_url)

        self.assertRegex(self.browser.current_url, '/projects/$')
        # and sees websites titele XP Tracker
        self.assertIn('Projects', self.browser.title)

        header2_text = self.browser.find_element_by_tag_name('h1').text
        self.assertEqual(header2_text, 'Create a new project')

    def test_can_see_new_project_form(self):
        self.browser.get(self.live_server_url)

        # form = self.browser.find_element_by_tag_name('form')

        input_title = self.find_element_by_field_id('title')
        # title_req = input_title.get_attribute('required')
        # self.assertEqual(title_req, 'true')

        self.assertEqual(
            input_title.get_attribute('placeholder'),
            'Projects title')

        input_description = self.find_element_by_field_id('description')

        # desc_req = input_description.get_attribute('required')
        # self.assertEqual(desc_req, 'true')

        self.assertEqual(
            input_description.get_attribute('placeholder'),
            'Projects description')

        input_release_date = self.find_element_by_field_id('release_date')
        # rel_date_req = input_release_date.get_attribute('required')
        # self.assertEqual(rel_date_req, 'true')

        self.assertEqual(
            input_release_date.get_attribute('placeholder'),
            'Projects release date'
        )

        input_identifier = self.find_element_by_field_id('identifier')
        # ident_req = input_identifier.get_attribute('required')
        # self.assertEqual(ident_req, 'true')
        self.assertEqual(
            input_identifier.get_attribute('placeholder'),
            'Projects identifier'
        )

        input_submit = self.browser.find_element_by_id('id_submit')
        self.assertEqual(input_submit.get_attribute('type'), 'submit')

    def test_can_create_new_project(self):
        project = self.create_new_project()
        base_project = BaseProjectModel()
        pid = project[PROJECT_ID]
        title = project[PROJECT_TITLE]
        descr = project[PROJECT_DESCR]
        release_date = project[PROJECT_RELEASE_DATE]
        self.go_to_project_home(project)
        self.assertRegex(
            self.browser.current_url, '/projects/%s/$' % pid)

        self.assertIn(title, self.browser.title)

        self.assertEqual(
            self.browser.find_element_by_id(base_project.fields_html_ids[PROJECT_TITLE]).text, title)

        self.assertEqual(
            self.browser.find_element_by_id(base_project.fields_html_ids[PROJECT_DESCR]).text, descr)

        self.assertEqual(
            self.browser.find_element_by_id(base_project.fields_html_ids[PROJECT_RELEASE_DATE]).text, release_date)

    def test_projects_index_page_has_project_rows(self):
        project = self.create_new_project()
        self.browser.get(self.live_server_url)
        self.browser.implicitly_wait(5)
        table = self.browser.find_element_by_id('id_list_projects')
        rows = table.find_elements_by_tag_name('tr')
        title = project[PROJECT_TITLE]
        self.assertIn(title, [row.text for row in rows])
        alink = self.browser.find_element_by_link_text(title)
        self.assertEqual(alink.text, title)

    def test_projects_index_links_redirects_to_project_home(self):
        project = self.create_new_project()
        title = project[PROJECT_TITLE]
        self.browser.get(self.live_server_url)
        import time
        time.sleep(10)
        alink = self.browser.find_element_by_link_text(title)
        alink.click()
        self.browser.implicitly_wait(5)
        heading = self.find_element_by_field_id(PROJECT_TITLE).text
        self.assertEqual(title, heading)


class ProjecValidationTest(BaseTest):

    def test_cannot_add_empty_vals(self):
        base_project = BaseProjectModel()
        fields = base_project.fields_html_ids
        self.browser.get(self.live_server_url)
        self.browser.find_element_by_id(fields[PROJECT_TITLE]).send_keys('\n')
        error = self.browser.find_elements_by_class_name('has-error')[0]
        self.assertEqual(error.text, ERROR_MESSAGES[PROJECT_TITLE]['required'])

    def test_can_not_add_past_release_date(self):
        project = self.create_new_project({'release_date': '1900-01-01'})
        self.browser.implicitly_wait(5)
        errors = self.browser.find_elements_by_class_name('has-error')
        # errors  has index same as order of fields. release_date id third in the
        #import pdb; pdb.set_trace()
        self.assertEqual(errors[2].text, ERROR_MESSAGES[PROJECT_RELEASE_DATE]['only_future'])
