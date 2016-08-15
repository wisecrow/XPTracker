from .base import BaseTest

class TaskCreateTest(BaseTest):
    def test_cannot_see_task_link_before_us_created(self):
        project = self.create_new_project()
        self.go_to_project_home(project)
        try:
            alink = self.browser.find_element_by_link_text('Tasks')
        except:
            alink = ''
        self.assertEquals('', alink)

    def test_can_see_tasks_link(self):
        project = self.create_new_project()
        us = self.create_new_us(project)
        self.go_to_iterations_home()
        self.create_new_iteration({'id_user_story': us['title']})
        self.go_to_project_home(project)
        alink = self.browser.find_element_by_link_text('Tasks')
        self.assertEqual(alink.text, 'Tasks')


    def test_tasks_link_is_correct(self):
        self.go_to_tasks_page()
        cur_url = self.browser.current_url
        self.assertRegex(cur_url, '/projects/.+/tasks/')

    def go_to_tasks_page(self):
        project = self.create_new_project()
        us = self.create_new_us(project)
        self.go_to_iterations_home()
        self.create_new_iteration({'id_user_story': us['title']})
        url = '%s/projects/%s/tasks/' % (self.live_server_url, project['identifier'])
        self.browser.get(url)

    def test_tests_page_shows_title(self):
        self.go_to_tasks_page()
        self.assertEqual(self.browser.title, 'Tasks')

    def test_tasks_show_html_form(self):
        self.go_to_tasks_page()
        title = self.browser.find_element_by_id('id_title')
        description = self.browser.find_element_by_id('id_description')
        estimate_time = self.browser.find_element_by_id('estimate_time')
        developer = self.browser.find_element_by_id('id_developoer')
        iteration = self.browser.find_element_by_id('id_iteration')





