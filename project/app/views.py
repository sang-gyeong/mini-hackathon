from django.shortcuts import render, redirect
from .models import Post_youtuber, Post_editor, Comment_editor, Comment_youtuber, Apply
from django.contrib.auth.models import User 
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from datetime import datetime
from project.settings import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_STORAGE_BUCKET_NAME, AWS_S3_REGION_NAME, AWS_S3_FILE_OVERWRITE
import boto3
from boto3.session import Session

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
    return render(request, 'list_youtuber.html', {'post_youtuber' : post_youtuber})

@login_required(login_url='/registration/login')
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

@login_required(login_url='/registration/login')
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
            reference = request.POST['reference']
        )
        return redirect(request, 'detail_editor')
    return render(request, 'form_to_editor.html')

def form_to_youtuber(request):
    if (request.method == 'POST'):
        Apply.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            author = request.user,
            datetime = datetime.now(),
            reference = request.POST['reference']
        )
        return redirect(request, 'detail_youtuber')
    return render(request, 'form_to_youtuber.html')

@login_required(login_url='/registration/login')
def new_editor(request):
    if (request.method == 'POST'):
        file_to_upload = request.FILES.get("img")
        session = Session(
        aws_access_key_id = AWS_ACCESS_KEY_ID,
        aws_secret_access_key = AWS_SECRET_ACCESS_KEY,
        region_name = AWS_S3_REGION_NAME
        )
        s3 = session.resource("s3")
        now = datetime.now().strftime("%Y%H%M%S")

        img_object = s3.Bucket(AWS_STORAGE_BUCKET_NAME).put_object(
            Key = str(request.user.pk)+'/'+now + file_to_upload.name,
            Body = file_to_upload
        )
        s3_url = "https://pyeon-an.s3.ap-northeast-2.amazonaws.com/"    

        new_post = Post_editor.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            author = request.user,
            datetime = datetime.now(),   
            tool = request.POST['tool'],
            work =request.POST['work'],
            career = request.POST['career'],
            genre = request.POST['genre'],
            rating = request.POST['rating'],
            img = s3_url+str(request.user.pk)+'/'+now + file_to_upload.name
        )
        return redirect('detail_editor', new_post.pk)

    return render(request, 'new_editor.html')

@login_required(login_url='/registration/login')
def new_youtuber(request):
    if (request.method == 'POST'):
        file_to_upload = request.FILES.get("img")
        session = Session(
        aws_access_key_id = AWS_ACCESS_KEY_ID,
        aws_secret_access_key = AWS_SECRET_ACCESS_KEY,
        region_name = AWS_S3_REGION_NAME
        )
        s3 = session.resource("s3")
        now = datetime.now().strftime("%Y%H%M%S")

        img_object = s3.Bucket(AWS_STORAGE_BUCKET_NAME).put_object(
            Key = str(request.user.pk)+'/'+now + file_to_upload.name,
            Body = file_to_upload
        )
        s3_url = "https://pyeon-an.s3.ap-northeast-2.amazonaws.com/" 
        
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
            img = s3_url+str(request.user.pk)+'/'+now + file_to_upload.name
        )
        return redirect('detail_youtuber', new_post.pk)

    return render(request, 'new_youtuber.html')


def edit_editor(request, post_pk):
    post = Post_editor.objects.get(pk=post_pk)
    
    if request.method == POST:
        file_to_upload = request.FILES.get("img")
        session = Session(
        aws_access_key_id = AWS_ACCESS_KEY_ID,
        aws_secret_access_key = AWS_SECRET_ACCESS_KEY,
        region_name = AWS_S3_REGION_NAME
        )
        s3 = session.resource("s3")
        now = datetime.now().strftime("%Y%H%M%S")

        img_object = s3.Bucket(AWS_STORAGE_BUCKET_NAME).put_object(
            Key = str(request.user.pk)+'/'+now + file_to_upload.name,
            Body = file_to_upload
        )
        s3_url = "https://pyeon-an.s3.ap-northeast-2.amazonaws.com/" 

        Post_editor.objects.filter(pk=post_pk).update(
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
            img = s3_url+str(request.user.pk)+'/'+now + file_to_upload.name
        )
        return redirect('detail_editor', post_pk)
    return render(request, 'edit_editor.html', {'post' : post})
        
def edit_youtuber(request, post_pk):
    post = Post_youtuber.objects.get(pk=post_pk)
    
    if request.method == POST:
        file_to_upload = request.FILES.get("img")
        session = Session(
        aws_access_key_id = AWS_ACCESS_KEY_ID,
        aws_secret_access_key = AWS_SECRET_ACCESS_KEY,
        region_name = AWS_S3_REGION_NAME
        )
        s3 = session.resource("s3")
        now = datetime.now().strftime("%Y%H%M%S")

        img_object = s3.Bucket(AWS_STORAGE_BUCKET_NAME).put_object(
            Key = str(request.user.pk)+'/'+now + file_to_upload.name,
            Body = file_to_upload
        )
        s3_url = "https://pyeon-an.s3.ap-northeast-2.amazonaws.com/" 

        Post_youtuber.objects.filter(pk=post_pk).update(
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
            img = s3_url+str(request.user.pk)+'/'+now + file_to_upload.name
        )
        return redirect('detail_youtuber', post_pk)
    return render(request, 'edit_youtuber.html', {'post' : post})

def mypage_youtuber(request, user_pk):
    post = Post_youtuber.objects.get(pk=user_pk)
    apply = Apply.objects.get(pk=user_pk)

    return render(request, 'mypage_youtuber.html', {'post' : post, 'apply' : apply})

def mypage_editor(request, user_pk):
    post = Post_editor.objects.get(pk=user_pk)
    apply = Apply.objects.get(pk=user_pk)

    return render(request, 'mypage_editor.html', {'post' : post, 'apply' : apply})

def signup(request):
    if request.method == "POST":
        found_user = User.objects.filter(username=request.POST['username'])
        if len(found_user) > 0:
            error = "아이디가 이미 존재합니다."
            return render(request, 'registration/signup.html', {'error' : error})

        new_user = User.objects.create_user(
            username = request.POST['username'],
            password = request.POST['password']
        )
        auth.login(request, new_user)
        return redirect('home')
    
    return render(request, 'registration/signup.html')


def login(request):
    if request.method == "POST":
        found_user = auth.authenticate(
            username = request.POST['username'],
            password = request.POST['password']
        )
        if found_user is None:
            error = "아이디 또는 비밀번호가 틀렸습니다."
            return render(request, 'registration/login.html', {'error' : error})

        auth.login(request, found_user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect(request.GET.get('next','/'))
    
    return render(request, 'registration/login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')

def payment(request):
    return render(request, 'payment.html')

def mypage_apply(request):
    return render(request, 'mypage_apply.html')

def mypage_contract(request):
    return render(request, 'mypage_contract.html')

def mypage_pay(request):
    return render(request, 'mypage_pay.html')

def chat(request):
    return render(request, 'chat.html')

