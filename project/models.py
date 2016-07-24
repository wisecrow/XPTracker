from django.db import models


class Project(models.Model):
    """Model for project."""

    title = models.TextField()
    description = models.TextField()
    release_date = models.DateField()
    identifier = models.TextField(unique=True)
