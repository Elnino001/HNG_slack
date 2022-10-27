from pydoc import classname
from wsgiref.validate import validator
from django.core.validators import MinValueValidator
from django.db import models

class HngSlackDetails(models.Model):
    slackUsername = models.CharField(max_length = 70)
    backend = models.BooleanField()
    age = models.IntegerField(validators=[MinValueValidator(1)])
    bio = models.TextField()
