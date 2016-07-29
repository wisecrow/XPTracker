# from unittest import skip

# from django.db.utils import  IntegrityError

from django.core.exceptions import ValidationError

from project.models import Project

from project.views import new_project

from .base import BaseTest


class ProjectModelTest(BaseTest):

    def test_canont_create_empty_fields(self):
        p = Project(title='')
        with self.assertRaises(ValidationError):
            p.full_clean()
            p.save()

    def test_empty_project_is_not_saved(self):
        self.client.post('/projects/new', data={'title': ''})
        self.assertEqual(Project.objects.count(), 0)


class ProjectCanCreateTest(BaseTest):
    """Class for project creation."""

    def test_can_create_and_retrieve_project(self):
        projects = BaseTest.projects_fields_vals
        for vals in BaseTest.projects_fields_vals:
            p = Project(
                title=vals[0],
                description=vals[1],
                release_date=vals[2],
                identifier=vals[3])
            p.save()

        for i, p in enumerate(Project.objects.all(), 0):
            self.assertEqual(p.title, projects[i][0])
            self.assertEqual(p.description, projects[i][1])
            self.assertEqual(
                p.release_date.strftime('%Y-%m-%d'),
                projects[i][2])
            self.assertEqual(p.identifier, projects[i][3])

    def test_can_create_project_from_post(self):
        data = BaseTest.projects_fields_vals[0]
        new_project(self.get_new_projects_request(data))

        self.assertEqual(Project.objects.count(), 1)
        p1 = Project.objects.first()
        self.assertEqual(p1.title, data[0])
        self.assertEqual(p1.description, data[1])
        self.assertEqual(p1.release_date.strftime('%Y-%m-%d'), data[2])
        self.assertEqual(p1.identifier, data[3])
