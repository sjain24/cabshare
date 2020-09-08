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
        postForm = PostForm()
        searchForm = SearchForm()
        commentForm = CommentForm()
        comments=Comment.objects.all()
        if request.GET.get('q') is not None:
            object_list = Post.objects.filter(
                Q(whereFrom__icontains=request.GET.get('whereFrom')) &
                Q(whereTo__icontains=request.GET.get('whereTo')) &
                Q(date__icontains=request.GET.get('date')) &
                Q(time__icontains=request.GET.get('time'))
            )
        else:
            object_list = Post.objects.all()
        args = {
            'postForm':postForm,
            'posts':object_list,
            'commentForm':commentForm,
            'comments':comments,
            'searchForm':searchForm
        }

    return render(request, 'cabPosts/posts.html', args)

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
        current_user = request.user
        comments = Comment.objects.all()
        args = {
            'postForm':postForm,
            'posts':posts ,
            'commentForm':commentForm,
            'comments':comments,
            'current_user':current_user
        }

    return render(request, 'cabPosts/my_posts.html', args)


def delete_my_post(request, key):
    post = Post.objects.get(id=key)
    print(post.id)
    post.delete()
    return redirect('cabPosts:my_posts_results')

def edit_my_post(request, key):
    post = Post.objects.get(id=key)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            #url = reverse('postpage', kwargs={'key': key})
            return redirect('cabPosts:my_posts_results')
        else:
            form = PostForm(instance=post)
    else:
        form = PostForm(instance=post)
    return render(request, 'cabPosts/edit_my_post.html', {'form':form, 'post':post})

