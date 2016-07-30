from project.models import Project

from user_stories.models import UserStory

from project.tests.base import BaseTest


class UserStoriesModelTest(BaseTest):

    def test_can_create_and_retrieve_us(self):
        project = self.create_new_project()
        us = UserStory(
            title='Nauja us',
            estimate_time=10,
            project=project
        )

        us.save()
        self.assertEqual(UserStory.objects.count(), 1)
        u1 = UserStory.objects.all()[0]
        self.assertEqual(u1.title, 'Nauja us')
        self.assertEqual(u1.project.title, project.title)
