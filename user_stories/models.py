from django.db import models
from project.models import Project

class UserStory(models.Model):
	title = models.TextField()
	estimate_time = models.IntegerField()
	project = models.ForeignKey(Project, on_delete=models.CASCADE)

# Create your models here.
