from project.models import Project

from user_stories.models import UserStory

from django.test import TestCase

from django.http import HttpRequest


PROJECT_TEST_VALS = {
    'title': 'My new project1',
    'description': 'My new project description1',
    'release_date': '2016-10-01',
    'identifier': 'my-new-procect1'
}

UserStory_VALS = {
    'title': 'Test title',
    'estimate_time': 3
}


class BaseTest(TestCase):
    project_fields = [
        'title',
        'description',
        'release_date',
        'identifier'
    ]

    projects_fields_vals = [
        ['My new project1', 'My new project description1', '2016-10-01', 'my-new-project1'],
        ['My new project2', 'My new project description2', '2016-10-02', 'my-new-project2'],
        ['My new project3', 'My new project description3', '2016-10-03', 'my-new-project3'],
        ['My new project4', 'My new project description4', '2016-10-04', 'my-new-project4']
    ]

    user_stories_fields = [
        'title',
        'estimate_time'
    ]

    user_stories_vals = [
        ['User story1', 1],
        ['User story2', 2],
        ['User story3', 3],
        ['User story4', 4]

    ]

    def get_new_projects_request(self, data):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['title'] = data[0]
        request.POST['description'] = data[1]
        request.POST['release_date'] = data[2]
        request.POST['identifier'] = data[3]
        return request

    def create_new_project(self):
        project = Project(
            title=PROJECT_TEST_VALS.get('title'),
            description=PROJECT_TEST_VALS.get('description'),
            release_date=PROJECT_TEST_VALS.get('release_date'),
            identifier=PROJECT_TEST_VALS.get('identifier'))
        project.save()
        return project

    def create_new_us(self, project):
        us = UserStory(
            title=UserStory_VALS['title'],
            estimate_time=UserStory_VALS['estimate_time'],
            project=project)
        us.save()
        return us

    def go_to_project_home(self, project):
        url = '/projects/%s/' % project.identifier
        return self.client.get(url)

    def go_to_us_home(self, project):
        url = '/projects/%s/user_stories/' % project.identifier
        return self.client.get(url)

    def go_to_iteration_home(self, project):
        url = '/projects/%s/iterations/' % project.identifier
        return self.client.get(url)




