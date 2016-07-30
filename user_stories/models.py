from django.core.urlresolvers import reverse

from django.db import models

from project.models import Project

USER_STORY_FIELDS = ['title', 'estimate_time']

class UserStory(models.Model):
    title = models.TextField()
    estimate_time = models.IntegerField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def get_absolute_url(self):
        #raise Exception, 'eeeeeeeeeeeeee'
        return reverse('show_projects')

# Create your models here.
