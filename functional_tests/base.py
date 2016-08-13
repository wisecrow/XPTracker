from selenium import webdriver

from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

# import unittest
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from selenium.webdriver.common.keys import Keys

from XPTracker.base import BaseProjectModel, PROJECT_TITLE, PROJECT_DESCR, PROJECT_RELEASE_DATE, PROJECT_ID
# from project.views import show_project
# from django.http import HttpRequest


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

    def find_element_by_field_id(self, field):
        base_project = BaseProjectModel()
        return self.browser.find_element_by_id(base_project.fields_html_ids[field])
