from selenium import webdriver

from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

# import unittest
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from selenium.webdriver.common.keys import Keys
# from project.views import show_project
# from django.http import HttpRequest


project_id_fields = [
    'id_title',
    'id_description',
    'id_release_date',
    'id_identifier'
]

projects_fields_vals = [
    ['My new project1', 'My new project description1', '2016-08-01', 'my-new-project1'],
    ['My new project2', 'My new project description2', '2016-08-02', 'my-new-project2'],
    ['My new project3', 'My new project description3', '2016-08-03', 'my-new-project3'],
    ['My new project4', 'My new project description4', '2016-08-04', 'my-new-project4']
]


user_stories_fields = [
    'id_title',
    'id_estimate_time'
]

user_stories_vals = [
    ['User story1', 1],
    ['User story2', 2],
    ['User story3', 3],
    ['User story4', 4]

]

PROOJECT_FIELD_ID_MAP = {
    'title': 'id_title',
    'description': 'id_description',
    'release_date': 'id_release_date',
    'identifier': 'id_identifier'
}

class BaseTest(StaticLiveServerTestCase):

    def setUp(self):
        binary = FirefoxBinary('/usr/bin/firefox')
        self.browser = webdriver.Firefox(firefox_binary=binary)
        # self.browser = webdriver.Firefox()

        # self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def create_new_model(self, fields, vals_vals, url, prefix={}):
        for vals in vals_vals:
            self.browser.get(url)
            for i, val in enumerate(vals, 0):
                val = vals[i]
                prf = prefix.get(fields[i], '')
                if prf:
                    val = '%s %s' % (val, prf)
                self.browser.find_element_by_id(fields[i]).send_keys(val)

            self.browser.find_element_by_id('id_submit').send_keys(Keys.ENTER)

    def create_new_projects(self):
        self.create_new_model(
            project_id_fields,
            projects_fields_vals,
            self.live_server_url
        )

    def find_element_by_field_id(self, field):
        return self.browser.find_element_by_id(PROOJECT_FIELD_ID_MAP[field])
