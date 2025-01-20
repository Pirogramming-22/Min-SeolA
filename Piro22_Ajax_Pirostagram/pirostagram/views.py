import os
from django.conf import settings
from django.shortcuts import render, redirect
from .models import Post, User, Like, Comment, Image
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json
from django.core.files.storage import default_storage

# Create your views here.
def signup(request):
    if request.method == 'POST':
        userid = request.POST.get('userid')
        password = request.POST.get('password')
        name = request.POST.get('name')
        default_profile_img_path = 'profile_images/default_profile.png'

        if User.objects.filter(userid=userid).exists():
            messages.error(request, "⚠️ 아이디가 이미 존재합니다.")
            return redirect('pirostagram:signup')

        user = User.objects.create_user(
            userid=userid,
            password=password,
            name=name,
            profileimg=default_profile_img_path,
        )

        auth_login(request, user)
        print(f"Logged in as: {request.user}")
        return redirect('pirostagram:profile')

    return render(request, 'pirostagram/signup.html')


def login(request):
    if request.method == 'POST':
        userid = request.POST.get('userid')
        password = request.POST.get('password')

        user = authenticate(request, userid=userid, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('pirostagram:profile')
        else:
            messages.error(request, "⚠️ 아이디 또는 비밀번호가 잘못되었습니다.")
            return redirect('pirostagram:login')

    return render(request, 'pirostagram/login.html')

@login_required
def profile(request):
    print(request.user)
    user = request.user
    posts = Post.objects.filter(user=user)
    followers_count = user.followers
    ctx = {
        'user': user,
        'posts': posts,
        'followers_count' : followers_count,
        'MEDIA_URL': settings.MEDIA_URL,  
    }
    return render(request, 'pirostagram/index.html', ctx)

@login_required
def create_post(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        images = request.FILES.getlist('images') 

        post = Post.objects.create(user=request.user, content=content)

        for image in images:
            img = Image.objects.create(image=image)
            post.images.add(img) 

        return redirect('pirostagram:profile') 

    return render(request, 'pirostagram/upload.html')

@csrf_exempt
def toggle_like(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        post_id = data.get('post_id')
        comment_id = data.get('comment_id') 

        user = request.user
        
        liked = False  
        likes_count = 0  

        try:
            if comment_id:
                comment = Comment.objects.get(id=comment_id)
                like, created = Like.objects.get_or_create(user=user, comment=comment)

                if not created:
                    like.delete() 
                else:
                    liked = True
                likes_count = comment.likes.count()  

            elif post_id:
                post = Post.objects.get(id=post_id)
                like, created = Like.objects.get_or_create(user=user, post=post)

                if not created:
                    like.delete() 
                else:
                    liked = True
                likes_count = post.likes.count()  

        except (Post.DoesNotExist, Comment.DoesNotExist):
            return JsonResponse({'error': '게시물 또는 댓글을 찾을 수 없습니다.'}, status=404)

        return JsonResponse({'liked': liked, 'likes_count': likes_count})

    return JsonResponse({'error': 'Invalid request'}, status=400)


def detail(request, post_id):
    post = Post.objects.get(id=post_id)
    user_has_liked_post = post.likes.filter(user=request.user).exists()
    

    comments = post.comments.all()
    for c in comments:
        c.liked_by_user = c.likes.filter(user=request.user).exists()
    
    context = {
        'post': post,
        'user_has_liked_post': user_has_liked_post,
        'comments': comments,  
    }
    return render(request, 'pirostagram/detail.html', context)


@csrf_exempt
def follow_toggle(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_id = data.get('user_id')
        action = data.get('action')

        try:
            user = User.objects.get(id=user_id)
            if action == 'follow':
                user.followers += 1
            elif action == 'unfollow':

                user.followers -= 1
            user.save()

            return JsonResponse({'success': True, 'followers_count': user.followers})
        except User.DoesNotExist:
            return JsonResponse({'success': False, 'error': '유저를 찾을 수 없습니다.'}, status=404)
    
    return JsonResponse({'success': False, 'error': '잘못된 요청입니다.'}, status=400)

@csrf_exempt
def add_comment(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        post_id = data.get('post_id')
        content = data.get('content')

    
        post = Post.objects.get(id=post_id)
        comment = Comment.objects.create(user=request.user, post=post, content=content)

        response_data = {
            'comment': {
                'id': comment.id,
                'userid': comment.user.userid,
                'profileimg': comment.user.profileimg.url,
                'content': comment.content,
                'likes_count': comment.likes.count(), 
                'user_has_liked': False, 
            }
        }
        return JsonResponse(response_data)
    
@csrf_exempt
def delete_comment(request):
    if request.method == "POST":
        data = json.loads(request.body)
        comment_id = data.get('comment_id')
        try:
            comment = Comment.objects.get(id=comment_id)
            comment.delete()
            return JsonResponse({"status": "success"})
        except Comment.DoesNotExist:
            return JsonResponse({"status": "fail", "message": "댓글이 존재하지 않습니다."}, status=404)
    return JsonResponse({"status": "fail"}, status=400)
