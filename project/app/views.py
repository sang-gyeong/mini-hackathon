from django.shortcuts import render
from .models import Post_youtuber, Post_editor, Comment
from django.contrib.auth.models import User 
from django.contrib import auth

# Create your views here.
def home(request):
    comment_editor = Comment_editor.objects.all
    post_editor = Post_editor.objects.all
    return render(request, 'home.html', {'comment_editor' : comment_editor, 'post_editor' : post_editor})


def list_editor(request):
    post_editor = Post_youtuber.objects.all
    return render(request, 'list_editor.html', {'post_editor' : post_editor})

