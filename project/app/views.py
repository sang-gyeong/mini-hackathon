from django.shortcuts import render
from .models import Post_youtuber, Post_editor, Comment
from django.contrib.auth.models import User 
from django.contrib import auth

# Create your views here.
def home(request):
    posts_youtuber = Post_youtuber.objects.all
    posts_editor = Post_editor.objects.all
    return render(request, 'home.html', {'posts_youtuber' : posts_youtuber, 'posts_editor' : posts_editor})

# def signup(request):
#     if (request.method == 'POST'):
#         found_user = User.objects.filter(username=request.POST['username'])
#         if (len(found_user)>0):
#             error = 'username이 이미 존재합니다'
#             return render(request, 'registration/signup.html', {'error' : error})

#         new_user = User.objects.create_user(
#             username = request.POST['username'],
#             password = request.POST['password']
#         )
#         auth.login(request, new_user)
#         return redirect('home')
#     return render(request, 'registration/signup.html')


# def login(request):
#     if (request.method == 'POST'):
#         found_user = auth.authenticate(
#             username = request.POST['username'],
#             password = request.POST['password']
#         )
#         if (found_user is None):
#             error = "아이디 또는 비밀번호가 틀렸습니다"
#             return render(request, 'registration/login.html', {'error' : error})

#         auth.login(
#             request,
#             found_user,
#             backend='django.contrib.auth.backends.ModelBackend')
#         return redirect(request.GET.get('next', '/'))
    
#     return render(request, 'registration/login.html')



# # def logout(request):
# #     auth.logout(request)
# #     return redirect('home')