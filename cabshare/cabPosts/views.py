from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from .forms import PostForm, CommentForm, SearchForm
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
    searchForm = SearchForm()
    comments=Comment.objects.all()
    if request.GET.get('whereFrom') is not None:
        where = request.GET.get('whereFrom')
        to = request.GET.get('whereTo')
        date = request.GET.get('date')
        time = request.GET.get('time')
        object_list = Post.objects.filter(
            Q(whereFrom__icontains=where) &
            Q(whereTo__icontains=to) &
            Q(date__icontains=date) &
            Q(time__icontains=time)
        )

    return render(request, 'cabPosts/search.html', {'form':searchForm, 'posts' : object_list ,'comments':comments})
