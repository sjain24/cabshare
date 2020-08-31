from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    whereFrom = models.CharField(max_length=255)
    whereTo = models.CharField(unique=True, max_length=255)
    date = models.DateField()
    time = models.TimeField(auto_now_add=True)
    flightOrTrainDetails = models.TextField()
    spaceLeft=models.IntegerField()
    peopleInterested=models.IntegerField()
    comments=models.IntegerField()