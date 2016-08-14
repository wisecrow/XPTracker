from selenium import webdriver

from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

# import unittest
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from selenium.webdriver.common.keys import Keys

from XPTracker.base import BaseProjectModel, PROJECT_TITLE, PROJECT_DESCR, PROJECT_RELEASE_DATE, PROJECT_ID, US_FIELDS_IDS

from selenium.webdriver.support.ui import WebDriverWait

# from project.views import show_project
# from django.http import HttpRequest

US_VALS = {'title': 'Test US title', 'estimate_time': 6}

class TestProjectVals(object):
    vals = [
        'test project1',
        'test project description1',
        '2020-01-01',
        'test-project1',
        ]

    def __init__(self, base_project):
        self.vals = self.set_vals(base_project)

    def set_vals(self, base_project):
        assert len(base_project.fields) == len(TestProjectVals.vals)
        test_vals = {}
        for i, field in enumerate(base_project.fields):
            test_vals[field] = TestProjectVals.vals[i]
        return test_vals


class BaseTest(StaticLiveServerTestCase):

    def setUp(self):
        binary = FirefoxBinary('/usr/bin/firefox')
        self.browser = webdriver.Firefox(firefox_binary=binary)
        # self.browser = webdriver.Firefox()

        # self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def create_new_model(self, fields, vals, url, data={}, prefix={}):
        self.browser.get(url)
        for field in vals.keys():
            val = data.get(field) or vals.get(field)
            prf = prefix.get(field, '')
            if prf:
                val = '%s %s' % (val, prf)

            self.wait_for_element_with_id(fields[field])

            self.browser.find_element_by_id(fields[field]).send_keys(val)
        self.browser.find_element_by_id('id_submit').send_keys(Keys.ENTER)
        return vals

    def create_new_project(self, data={}):
        base_project = BaseProjectModel()
        test_project_vals = TestProjectVals(base_project).vals
        return self.create_new_model(
            base_project.fields_html_ids,
            test_project_vals,
            self.live_server_url,
            data
        )

    def create_new_us(self, project, data={}):
        return self.create_new_model(
            US_FIELDS_IDS,
            US_VALS,
            self.get_project_us_url(project),
            data
        )

    def wait_for_element_with_id(self, element_id):
        WebDriverWait(self.browser, timeout=30).until(
            lambda b: b.find_element_by_id(element_id)
        )


    def get_project_us_url(self, project):
        return '%s/projects/%s/user_stories/' % (self.live_server_url, project[PROJECT_ID])

    def find_element_by_field_id(self, field):
        base_project = BaseProjectModel()
        return self.browser.find_element_by_id(base_project.fields_html_ids[field])


    def go_to_project_home(self, project):
        self.browser.get(
            '%s/projects/%s/' % (self.live_server_url, project[PROJECT_ID]))
