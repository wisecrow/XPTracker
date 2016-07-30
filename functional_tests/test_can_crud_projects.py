from unittest import skip

from project.models import PROJECT_FIELDS

from project.forms import ERROR_MESSAGES

from functional_tests.base import BaseTest, projects_fields_vals, \
    project_id_fields

from .base import PROOJECT_FIELD_ID_MAP

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
        self.create_new_projects()
        for vals in projects_fields_vals:
            self.browser.get(
                '%s/projects/%s/' % (self.live_server_url, vals[3]))
            self.assertRegex(
                self.browser.current_url, '/projects/%s/$' % vals[3])

            id_fields = project_id_fields
            self.assertIn(vals[0], self.browser.title)

            self.assertEqual(
                self.browser.find_element_by_id(id_fields[0]).text, vals[0])

            self.assertEqual(
                self.browser.find_element_by_id(id_fields[1]).text, vals[1])

            self.assertEqual(
                self.browser.find_element_by_id(id_fields[2]).text, vals[2])

    def test_projects_index_page_has_project_rows(self):
        self.create_new_projects()
        self.browser.get(self.live_server_url)
        table = self.browser.find_element_by_id('id_list_projects')
        rows = table.find_elements_by_tag_name('tr')
        for vals in projects_fields_vals:
            self.assertIn(vals[0], [row.text for row in rows])
            alink = self.browser.find_element_by_link_text(vals[0])
            self.assertEqual(alink.text, vals[0])

    def test_projects_index_links_redirects_to_project_home(self):
        self.create_new_projects()
        for vals in projects_fields_vals:
            self.browser.get(self.live_server_url)
            alink = self.browser.find_element_by_link_text(vals[0])
            alink.click()
            self.browser.implicitly_wait(10)
            heading = self.find_element_by_field_id('title').text
            self.assertEqual(vals[0], heading)


class ProjecValidationTest(BaseTest):

    def test_cannot_add_empty_vals(self):
        for i, field in enumerate(PROJECT_FIELDS, 0):
            self.browser.get(self.live_server_url)

            #import pdb; pdb.set_trace()
            self.browser.implicitly_wait(10)
            self.find_element_by_field_id(field).send_keys('\n')
            error = self.browser.find_elements_by_class_name('has-error')[i]
            self.assertEqual(error.text, ERROR_MESSAGES[field]['required'])


