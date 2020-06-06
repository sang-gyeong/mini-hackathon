from django.shortcuts import render
from .models import Post_youtuber, Post_editor, Comment
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    comment = 
    posts_editor = Post_editor.objects.all
    return render(request, 'home.html', {'posts_youtuber' : posts_youtuber, 'posts_editor' : posts_editor})

def list_editor(request)