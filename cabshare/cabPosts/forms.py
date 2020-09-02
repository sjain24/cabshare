from django import forms
from django.forms import ModelForm
from .models import Post, Comment


class PostForm(forms.ModelForm):
    whereFrom = forms.CharField(max_length=255)
    whereTo = forms.CharField(max_length=255)
    date = forms.DateField()
    time = forms.TimeField()
    flightOrTrainDetails = forms.CharField(required=True)
    spaceLeft=forms.IntegerField(initial=3)
    #peopleInterested=forms.IntegerField(default=0)

    class Meta:
        model = Post
        fields = {'whereFrom','whereTo', 'date','time','flightOrTrainDetails',}

class CommentForm(forms.ModelForm):
    content = forms.CharField(max_length=500)

    class Meta:
        model = Comment
        fields={'content',}
