from functional_tests.base import BaseTest
from users.models import FIELDS
from users.forms import FIELDS_IDS, ERROR_MESSAGES
from XPTracker.base import PROJECT_TITLE, PROJECT_DESCR, PROJECT_RELEASE_DATE, PROJECT_ID

class ProjectPageTest(BaseTest):

    def test_developers_index_url_is_correct(self):
        project = self.create_new_project()
        self.go_to_project_home(project)
        self.browser.get(self.live_server_url)
        title = project[PROJECT_TITLE]
        self.browser.find_element_by_link_text(title).click()
        self.browser.implicitly_wait(10)
        alink = self.browser.find_element_by_link_text('Developers').click()
        cur_url = self.browser.current_url
        self.assertRegex(cur_url, '/projects/.+/developers/')



    def test_developers_index_shows_form(self):
        project = self.create_new_project()
        title = project[PROJECT_TITLE]
        self.browser.get(self.live_server_url)
        self.browser.find_element_by_link_text(title).click()
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

    def test_show_list_of_devs_after_form_submit(self):
        project = self.create_new_project()
        title = project[PROJECT_TITLE]
        self.browser.get(self.live_server_url)
        self.browser.find_element_by_link_text(title).click()
        self.browser.implicitly_wait(10)
        alink = self.browser.find_element_by_link_text('Developers').click()
        self.browser.find_element_by_id('id_firstname').send_keys("Aloysius")
        self.browser.find_element_by_id('id_lastname').send_keys('Proscorus')
        email = 'ciber@gmail.com'
        self.browser.find_element_by_id('id_email').send_keys(email)
        self.browser.find_element_by_id('id_submit').click()
        table = self.browser.find_element_by_id('id_list_developers')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('Aloysius Proscorus', [row.text for row in rows])

class DeveloperValidationTest(BaseTest):

    def test_cannot_add_empty_vals(self):
        project = self.create_new_project()
        url = '%s/projects/%s/developers/' % (self.live_server_url, project[PROJECT_ID])
        self.browser.get(url)
        for ii, field in enumerate(FIELDS):
            self.browser.implicitly_wait(10)
            self.browser.find_element_by_id(FIELDS_IDS.get(field)).send_keys('\n')
            #import time
            #time.sleep(10)
            self.browser.find_element_by_id('id_submit').click()
            error = self.browser.find_elements_by_class_name('has-error')[ii]
            self.assertEqual(error.text, ERROR_MESSAGES[field]['required'])
