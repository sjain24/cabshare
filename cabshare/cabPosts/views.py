from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import PostForm, CommentForm
from .models import Post, Comment
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def get_posts(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        postForm=PostForm(request.POST)
        if postForm.is_valid():
            # code
            return HttpResponseRedirect('/thanks/')
    # if a GET (or any other method) we'll create a blank form
    else:
        postForm = PostForm()
        #current_user = request.user
        posts = Post.objects.all()
        #commentForm = CommentForm()
        #comments = Comment.objects.all()
        args = {'postForm':postForm, 'posts':posts ,}

    return render(request, 'cabPosts/post.html', args)
