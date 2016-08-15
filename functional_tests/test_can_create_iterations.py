from .base import BaseTest

class IterationCreateTest(BaseTest):

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
        us = self.go_to_iterations_home()
        self.create_new_iteration({'id_user_story': us['title']})
        table = self.browser.find_element_by_id('id_list_iterations')
        rows = table.find_elements_by_tag_name('tr')
        title = 'Iteration title'
        self.assertIn(title, [row.text for row in rows])





