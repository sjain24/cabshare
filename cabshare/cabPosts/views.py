from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import PostForm, CommentForm
from .models import Post, Comment
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


@login_required
def get_posts(request):
    if request.method == 'POST':
        if 'post' in request.POST:
            postForm = PostForm(request.POST)
            if postForm.is_valid():
                post = postForm.save(commit=False)
                post.author = request.user
                post.save()
                
            return redirect('cabPosts:posts')
        else:
            commentForm=CommentForm(request.POST)
            
            if commentForm.is_valid():
                post_id = request.POST['post_id']
                post_instance = get_object_or_404(Post, id=post_id)
                comment = commentForm.save(commit=False)
                comment.name = request.user
                comment.post = post_instance
                comment.save()
                return redirect('cabPosts:posts')
            else:
                return render(request,'500.html',{})

    else:
        postForm = PostForm()
        posts = Post.objects.all()
        commentForm = CommentForm()
        comments=Comment.objects.all()
        args = {'postForm':postForm, 'posts':posts ,'commentForm':commentForm,'comments':comments}

    return render(request, 'cabPosts/post.html', args)
