from django.core.urlresolvers import reverse

from XPTracker.base import PROJECT_TITLE, PROJECT_DESCR, PROJECT_RELEASE_DATE, PROJECT_ID

from django.db import models

FIELDS = [PROJECT_TITLE, PROJECT_DESCR, PROJECT_RELEASE_DATE, PROJECT_ID]

class Project(models.Model):
    """Model for project."""

    title = models.TextField()
    description = models.TextField()
    release_date = models.DateField()
    identifier = models.SlugField(unique=True)

    def get_absolute_url(self):
        return reverse('show_project', args=[self.identifier])
