from django.shortcuts import render
from .models import Post, Comment


from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
# Create your views here.import
from cabPosts.forms import PostForm, CommentForm
from cabPosts.models import Post, Comment
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

class HomeView(TemplateView):
    template_name = './templates/pages/home.html'

    def get(self, request):
        postForm = PostForm()
        current_user = request.user
        posts = Post.objects.all().order_by('-date')
        commentForm = CommentForm()
        comments = Comment.objects.all()
        args = {'postForm':postForm, 'posts':posts , 'users':users, 'commentForm':commentForm, 'comments':comments , }

        return render(request, self.template_name, args)

    def createNewPost(self , request):
        postForm = PostForm(request.POST)
        if postForm.is_valid():
            post = postForm.save(commit=False)
            post.author = request.user
            post.save()
            text = postForm.cleaned_data['post']
            postForm = PostForm()
            return redirect('home:home')

        args = {'postForm': postForm, 'text': text }
        return render(request, self.template_name,args)

    def createNewComment(self , request):
        commentForm = CommentForm(request.POST)
        if commentForm.is_valid():
            comment = commentForm.save(commit=False)
            comment.comment_author = request.user
          #?  comment.email = request.
            post.save()
            text = postForm.cleaned_data['post']
            postForm = PostForm()
            return redirect('home:home')

        args = {'postForm': postForm, 'text': text }
        return render(request, self.template_name,args)
