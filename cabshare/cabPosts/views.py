from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import PostForm, CommentForm
from .models import Post, Comment
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Q


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
                comment.email = request.user.email
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

    return render(request, 'cabPosts/posts.html', args)

@login_required
def get_search_results(request):
    object_list = []
    commentForm = CommentForm()
    comments=Comment.objects.all()
    if request.method=='GET':
        if request.GET.get('q') is not None:
            query = request.GET.get('q')
            object_list = Post.objects.filter(
                Q(whereFrom__icontains=query) | 
                Q(whereTo__icontains=query) |
                Q(date__icontains=query) |
                Q(time__icontains=query) |
                Q(flightOrTrainDetails__icontains=query)
            )
            
        return render(request, 'cabPosts/search.html', {'posts' : object_list ,'comments':comments,'commentForm':commentForm})
    else:
        if request.method=='POST':
            commentForm=CommentForm(request.POST)
            if commentForm.is_valid():
                post_id = request.POST['post_id']
                post_instance = get_object_or_404(Post, id=post_id)
                comment = commentForm.save(commit=False)
                comment.name = request.user
                comment.post = post_instance
                comment.email = request.user.email
                comment.save()
                return redirect('cabPosts:posts')
                #return render(request, 'cabPosts/search.html', {'posts' : object_list ,'comments':comments,'commentForm':commentForm})
            else:
                return render(request,'500.html',{})
        else:
            return render(request, 'cabPosts/search.html', {'posts' : object_list ,'comments':comments,'commentForm':commentForm})

@login_required
def get_my_posts(request):
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
                comment.email = request.user.email
                comment.save()
                return redirect('cabPosts:posts')
            else:
                return redirect('cabPosts:my_posts')

    else:
        postForm = PostForm()
        posts = Post.objects.all()
        commentForm = CommentForm()
        current_user=request.user
        comments=Comment.objects.all()
        args = {'postForm':postForm, 'posts':posts ,'commentForm':commentForm,'comments':comments,'current_user':current_user}

    return render(request, 'cabPosts/my_posts.html', args)
def delete_my_post(request,key):
    post = Post.objects.get(id=key)
    print(post.id)
    post.delete()
    return redirect('cabPosts:my_posts_results')

