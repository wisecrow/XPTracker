from .base import BaseTest
from project.models import Project
from django.core.exceptions import ValidationError
from django.db.utils import  IntegrityError
from unittest import skip


class ProjectModelTest(BaseTest):
	def test_canont_create_empty_fields(self):
		p=Project(title='')
		with self.assertRaises(ValidationError):
			p.full_clean()
			p.save()

			# run full validation, because SQLite does'nt enforce it


