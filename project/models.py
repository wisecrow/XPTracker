from django.core.urlresolvers import reverse

from django.db import models

PROJECT_FIELDS = ['title', 'description', 'release_date', 'identifier']

class Project(models.Model):
    """Model for project."""

    title = models.TextField()
    description = models.TextField()
    release_date = models.DateField()
    identifier = models.TextField(unique=True)

    def get_absolute_url(self):
        return reverse('show_project', args=[self.identifier])
