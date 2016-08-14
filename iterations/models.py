from django.db import models
from project.models import Project
from user_stories.models import UserStory


class Iteration(models.Model):

    title = models.TextField()
    duration = models.IntegerField()
    user_story = models.ForeignKey(UserStory, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)