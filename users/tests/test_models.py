from project.tests.base import BaseTest
from users.models import Developer

class CreateDeveloperTest(BaseTest):

    def test_cant_create_and_retriev_dev(self):
        dev = Developer(
            firstname='Tadas',
            lastname='Pukys',
            email='pukislavas@sdsd.lt'
     )
        dev.save()
        self.assertEqual(Developer.objects.count(), 1)