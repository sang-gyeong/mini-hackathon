from django.shortcuts import render
from .models import Post_youtuber, Post_editor, Comment
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    comment_editor = Comment_editor.object.all
    post_editor = Post_editor.objects.all
    return render(request, 'home.html', {'post_editor' : post_editor, 'comment_editor' : comment_editor})
