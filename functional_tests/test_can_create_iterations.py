from .base import BaseTest
from selenium.webdriver.common.keys import Keys
from project.models import Project
from user_stories.models import UserStory

class IterationCreateTest(BaseTest):

    def go_to_iterations_home(self):
        project = self.create_new_project()
        self.go_to_project_home(project)
        us = self.create_new_us(project)
        self.go_to_project_home(project)
        self.browser.implicitly_wait(5)
        self.browser.find_element_by_link_text('Iterations').click()
        return project

    def test_cannot_see_iter_link_before_us_created(self):
        project = self.create_new_project()
        self.go_to_project_home(project)
        try:
            alink = self.browser.find_element_by_link_text('Iterations')
        except:
            alink = ''
        self.assertEquals('', alink)

        self.create_new_us(project)
        self.go_to_project_home(project)
        alink = self.browser.find_element_by_link_text('Iterations')
        self.assertEqual(alink.text, 'Iterations')

    def test_iter_link_is_correct(self):
        self.go_to_iterations_home()
        cur_url = self.browser.current_url
        self.assertRegex(cur_url, '/projects/.+/iterations/')

    def test_iter_page_shows_html_form(self):
        self.go_to_iterations_home()
        self.assertIn('Iterations', self.browser.title)
        form = self.browser.find_element_by_tag_name('form')
        title_input = self.browser.find_element_by_id('id_title')
        duration_input = self.browser.find_element_by_id('id_duration')
        user_story_input = self.browser.find_element_by_id('id_user_story')

    def test_can_create_and_see_iteration(self):
        project_dict = self.go_to_iterations_home()
        projects = Project.objects.filter(identifier=project_dict['identifier'])
        project = projects[0]
        user_story = UserStory.objects.filter(project=project)[0]

        self.browser.find_element_by_id('id_title').send_keys('Iteration title')
        self.browser.find_element_by_id('id_duration').send_keys(1)
        self.browser.find_element_by_id('id_user_story').send_keys(user_story.title)
        self.browser.find_element_by_id('id_submit').send_keys(Keys.ENTER)
        table = self.browser.find_element_by_id('id_list_iterations')
        rows = table.find_elements_by_tag_name('tr')
        title = 'Iteration title'
        self.assertIn(title, [row.text for row in rows])


