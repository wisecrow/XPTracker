from iterations.models import Iteration
from project.tests.base import BaseTest


class IterationModelTest(BaseTest):

    def test_cant_create_iteraion(self):
        project = self.create_new_project()
        us = self.create_new_us(project)
        iter_title = 'Iter title'
        iteration = Iteration(
            title=iter_title,
            duration=2,
            user_story=us,
            project=project)
        iteration.save()
        self.assertEqual(Iteration.objects.count(), 1)
        iteration1 = Iteration.objects.all()[0]
        self.assertEqual(iteration1.title, iter_title)