from django.db import models



class Post(models.Model):
    whereFrom = models.CharField(max_length=255)
    whereTo = models.CharField(unique=True, max_length=255)
    date = models.DateField()
    time = models.TimeField(auto_now_add=True)
    flightOrTrainDetails = models.TextField()
    spaceLeft=models.IntegerField()
    peopleInterested=models.IntegerField()
    comments=models.TextField()