from .base import BaseTest

class IterationCreateTest(BaseTest):

    def go_to_iterations_home(self):
        project = self.create_new_project()
        self.go_to_project_home(project)
        self.create_new_us(project)
        self.go_to_project_home(project)
        self.browser.implicitly_wait(5)
        self.browser.find_element_by_link_text('Iterations').click()        

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
