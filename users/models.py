from django.db import models

FIELDS = ['firstname', 'lastname', 'email']

class Developer(models.Model):

    firstname = models.TextField()
    lastname = models.TextField()
    email = models.EmailField(unique=True)
# Create your models here.
