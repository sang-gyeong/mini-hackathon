from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post_youtuber(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    datetime = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='youtuber')
    img = models.TextField()
    tool = models.TextField()
    work = models.TextField()
    career = models.TextField()
    period = models.TextField()
    genre = models.TextField()
    rating = models.ForeignKey(Comment_youtuber, on_delete=models.CASCADE, related_name='ratings_y')

    def __str__(self):
        return self.title

class Post_editor(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    datetime = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='editor')
    img = models.TextField()
    tool = models.TextField()
    work = models.TextField()
    career = models.TextField()
    period = models.TextField()
    genre = models.TextField()
    rating = models.ForeignKey(Comment_editor, on_delete=models.CASCADE, related_name='ratings_e')

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

