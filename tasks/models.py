from django.db import models
from users.models import Developer
from iterations.models import Iteration

class Task(models.Model):
    title = models.TextField()
    description = models.TextField()
    estimate_time = models.FloatField()
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE)
    iteration = models.ForeignKey(Iteration, on_delete=models.CASCADE)
