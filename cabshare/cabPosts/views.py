from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import PostForm, CommentForm
from .models import Post, Comment
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def get_posts(request):
    if request.method == 'POST':
        postForm=PostForm(request.POST)
        if postForm.is_valid():
            post = postForm.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('cabPosts:posts')
        else:
            return render(request,'500.html',{})

    else:
        postForm = PostForm()
        posts = Post.objects.all()
        commentForm = CommentForm()
        #comments=Comment.objects.all()
        args = {'postForm':postForm, 'posts':posts ,'commentForm':commentForm,}

    return render(request, 'cabPosts/post.html', args)
