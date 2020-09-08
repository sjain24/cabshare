from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth import get_user_model as user_model
User = user_model()
#from users.models import User

class Post(models.Model):
    whereFrom = models.CharField(max_length=255)
    whereTo = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    flightOrTrainDetails = models.TextField(blank=True)
    spaceLeft=models.IntegerField(default=3)
    peopleInterested=models.IntegerField(default=0)
    author = models.ForeignKey(User , on_delete=models.CASCADE)

    class meta:
        app_label  = 'cabPosts'

    def __str__(self):
        return self.whereFrom + '-' +self.whereTo + 'on '+ str(self.date)+ ' at '+str(self.time)
   # comments=models.TextField()
   
   ## def savePost(self, *args, **kwargs):
        #super(Post, self).save(*args, **kwargs)

class Comment(models.Model):
    name = models.ForeignKey(User , on_delete=models.CASCADE)
    email = models.EmailField()
    content = models.TextField(max_length=500)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content + ' by ' + ' on post '+ str(self.post.pk)
