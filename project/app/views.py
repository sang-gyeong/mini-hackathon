from django.shortcuts import render, redirect
from .models import Post_youtuber, Post_editor, Comment_editor, Comment_youtuber, Apply
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

    if request.method == "POST":
        Comment_youtuber.objects.create(
           post = post,
           content = request.POST['content'],
           author = request.user,
           rate = request.POST['rate'],
           datetime = datetime.now(),
        )
        return redirect('detail_youtuber', post_pk)
    return render(request, 'detail_youtuber.html', {'post' : post})



def form_to_editor(request):
    if (request.method == 'POST'):
        Apply.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            author = request.user,
            datetime = datetime.now(),
            img = request.POST['img']
        )
        return redirect(request, 'detail_editor')


def new_editor(request):
    if (request.method == 'POST'):
        new_post = Post_editor.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            author = request.user,
            datetime = datetime.now(),   
            tool = request.POST['tool'],
            work =request.POST['work'],
            career = request.POST['career'],
            period = request.POST['period'],
            genre = request.POST['genre'],
            rating = request.POST['rating'],
            img = request.POST['img'],
        )
        return redirect('detail_editor', new_post.pk)

    return render(request, 'new_editor.html')


def new_youtuber(request):
    if (request.method == 'POST'):
        new_post = Post_youtuber.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            author = request.user,
            datetime = datetime.now(),   
            tool = request.POST['tool'],
            work =request.POST['work'],
            career = request.POST['career'],
            period = request.POST['period'],
            genre = request.POST['genre'],
            rating = request.POST['rating'],
            img = request.POST['img'],
        )
        return redirect('detail_youtuber', new_post.pk)

    return render(request, 'new_youtuber.html')


def edit_editor(request):
    if (request.method )