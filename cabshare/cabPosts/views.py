from django.shortcuts import render
#from .models import Post, Comment

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
# Create your views here.import
from .forms import PostForm, CommentForm
from .models import Post, Comment
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# class HomeView(TemplateView):
#     template_name = 

#     def get(self, request):
#         postForm = PostForm()
#         current_user = request.user
#         posts = Post.objects.all().order_by('-date')
#         commentForm = CommentForm()
#         comments = Comment.objects.all()
#         args = {'postForm':postForm, 'posts':posts , 'users':users, 'commentForm':commentForm, 'comments':comments , }

#         return render(request, self.template_name, args)

#     def post(self , request):
#         postForm = PostForm(request.POST)
#         if postForm.is_valid():
#             post = postForm.save(commit=False)
#             post.author = request.user
#             post.save()
#             text = postForm.cleaned_data['post']
#             postForm = PostForm()
#             return redirect('home:home')

#         args = {'postForm': postForm, 'text': text }
#         return render(request, self.template_name,args)

#     def createNewComment(self , request):
#         commentForm = CommentForm(request.POST)
#         if commentForm.is_valid():
#             comment = commentForm.save(commit=False)
#             comment.comment_author = request.user
#           #?  comment.email = request.
#             post.save()
#             text = postForm.cleaned_data['post']
#             postForm = PostForm()
#             return redirect('home:home')

#         args = {'postForm': postForm, 'text': text }
#         return render(request, self.template_name,args)

def get_posts(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        postForm=PostForm(request.POST)
        if postForm.is_valid():
            # post = postForm.save(commit=False)
            # post.author = request.user
            # post.save()
            # text = postForm.cleaned_data['post']
            # postForm = PostForm()
            #return redirect('home:home')

        # check whether it's valid:
        #if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')
    # if a GET (or any other method) we'll create a blank form
    else:
        postForm = PostForm()
        #current_user = request.user
        posts = Post.objects.all()
        #commentForm = CommentForm()
        #comments = Comment.objects.all()
        args = {'postForm':postForm, 'posts':posts ,}

    return render(request, 'cabPosts/posts.html', args)

