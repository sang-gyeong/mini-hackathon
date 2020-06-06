from django.shortcuts import render, redirect
from .models import Post_youtuber, Post_editor, Comment_editor, Comment_youtuber
from django.contrib.auth.models import User 
from django.contrib import auth
from datetime import datetime

# Create your views here.
def home(request):
    comment_editor = Comment_editor.objects.all
    post_editor = Post_editor.objects.all
    return render(request, 'home.html', {'comment_editor' : comment_editor, 'post_editor' : post_editor})


def list_editor(request):
    post_editor = Post_editor.objects.all
    return render(request, 'list_editor.html', {'post_editor' : post_editor})

def list_youtuber(request):
    post_youtuber = Post_youtuber.objects.all
    return render(request, 'list_editor.html', {'post_youtuber' : post_youtuber})

def detail_editor(request, post_pk):
    post = Post_editor.objects.get(pk=post_pk)

    if request.method == "POST":
        Comment_editor.objects.create(
           post = post,
           content = request.POST['content'],
           author = request.user,
           rate = request.POST['rate'],
           datetime = datetime.now()
        )
        return redirect('detail_editor', post_pk)
    return render(request, 'detail_editor.html', {'post' : post})


def detail_youtuber(request, post_pk):
    post = Post_youtuber.objects.get(pk=post_pk)

<<<<<<< HEAD

=======
    if request.method == "POST":
        Comment_youtuber.objects.create(
           post = post,
           content = request.POST['content'],
           author = request.user,
           rate = request.POST['rate'],
           datetime = datetime.now()
        )
        return redirect('detail_youtuber', post_pk)
    return render(request, 'detail_youtuber.html', {'post' : post})
>>>>>>> 692931619100ab310f0e63243aab7371cb2bf3d8
