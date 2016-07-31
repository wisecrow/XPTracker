from django.db import models

class Developer(models.Model):

    firstname=models.TextField()
    lastname = models.TextField()
    email = models.EmailField(unique=True)
# Create your models here.
