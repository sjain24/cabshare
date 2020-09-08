from django import forms
from .models import Post, Comment
from django.utils import timezone

CHOICES = [
    ('Airport','Airport'),
    ('Campus','Campus'),
    ('Railway Station','Railway station'),
]
class PostForm(forms.ModelForm):
    whereFrom = forms.CharField(label="From", widget=forms.Select(choices=CHOICES), required = True, initial=CHOICES[0] )
    whereTo = forms.CharField(label="To", widget=forms.Select(choices=CHOICES), required = True, initial=CHOICES[1])
    date = forms.DateField(initial=timezone.now(), widget = forms.SelectDateWidget, required = True)
    time = forms.TimeField(initial=timezone.now(), required = True)
    flightOrTrainDetails = forms.CharField(label = "Details", required = False)
    spaceLeft=forms.IntegerField(initial=3, required = True, min_value = 0)
    #peopleInterested=forms.IntegerField(default=0)
    field_order = ['whereFrom','whereTo', 'date','time','flightOrTrainDetails', 'spaceLeft',]
    class Meta:
        model = Post
        fields = {'whereFrom','whereTo', 'date','time','flightOrTrainDetails', 'spaceLeft',}

class CommentForm(forms.ModelForm):
    content = forms.CharField(label="Add comment", max_length=500)

    class Meta:
        model = Comment
        fields={'content',}

class SearchForm(forms.Form):
    whereFrom = forms.CharField(label="From", widget=forms.Select(choices=CHOICES), required = True, initial=CHOICES[0])
    whereTo = forms.CharField(label="To", widget=forms.Select(choices=CHOICES), required = False, initial=CHOICES[1])
    date = forms.DateField(initial=timezone.now(), required = False)
    time = forms.TimeField(initial=timezone.now(), required = False)
