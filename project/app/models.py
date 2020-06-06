from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post_youtuber(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    datetime = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='youtuber')
    img = models.TextField(null=True)
    tool = models.TextField(null=True) 
    work = models.TextField(null=True) 
    career = models.TextField(null=True)
    period = models.TextField(null=True)
    genre = models.TextField(null=True)
    rating = models.TextField(null=True)

    def __str__(self):
        return self.title

class Post_editor(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(null=True)
    datetime = models.DateTimeField(null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='editor')
    img = models.TextField(null=True)
    tool = models.TextField(null=True)
    work = models.TextField(null=True)
    career = models.TextField(null=True)
    period = models.TextField(null=True)
    genre = models.TextField(null=True)
    rating = models.TextField(null=True)

    def __str__(self):
        return self.title

class Comment_youtuber(models.Model):
    post = models.ForeignKey(Post_youtuber, on_delete=models.CASCADE, related_name='comments_y')
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments_y')
    rate = models.IntegerField()
    datetime = models.DateTimeField()

class Comment_editor(models.Model):
    post = models.ForeignKey(Post_editor, on_delete=models.CASCADE, related_name='comments_e')
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments_e')
    rate = models.IntegerField()
    datetime = models.DateTimeField()
