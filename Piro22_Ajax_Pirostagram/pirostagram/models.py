from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
import random


class UserManager(BaseUserManager):
    def create_user(self, userid, password=None, **extra_fields):
        if not userid:
            raise ValueError('아이디는 필수 항목입니다.')
        user = self.model(userid=userid, **extra_fields)
        user.set_password(password)  
        user.save(using=self._db)
        return user

    def create_superuser(self, userid, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(userid, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    userid = models.CharField("아이디", max_length=20, unique=True)
    name = models.CharField("이름", max_length=50)
    profileimg = models.ImageField(upload_to='profile_images/', default='profile_images/default_profile.png')
    followers = models.PositiveIntegerField("팔로워 수", default=random.randint(50, 600))

    objects = UserManager()
    USERNAME_FIELD = 'userid' 
    REQUIRED_FIELDS = ['name']

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, verbose_name="게시한 유저", on_delete=models.CASCADE, related_name='post_user')
    images = models.ManyToManyField('Image', related_name='posts', blank=True)  # 여러 이미지를 처리
    content = models.TextField("게시글 내용")
    created_at = models.DateTimeField("작성일", auto_now_add=True)

    @property
    def likes_count(self):
        return self.likes.count()



class Image(models.Model):
    image = models.ImageField(upload_to='post_images/', verbose_name="이미지")

class Comment (models.Model):
    user = models.ForeignKey(User, verbose_name="댓글 단 유저", on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, verbose_name="게시글", on_delete=models.CASCADE, related_name='comments')
    parent = models.ForeignKey(
        'self', verbose_name="상위 댓글", null=True, blank=True, on_delete=models.CASCADE, related_name='replies'
    )
    content = models.TextField("댓글 내용")
    created_at = models.DateTimeField("작성일", auto_now_add=True)

    @property
    def likes_count(self):
        return self.likes.count()
    


class Like(models.Model):
    user = models.ForeignKey(User, verbose_name="좋아요 한 유저", on_delete=models.CASCADE, related_name='likes')
    post = models.ForeignKey(Post, verbose_name="게시글", on_delete=models.CASCADE, related_name='likes', null=True, blank=True)
    comment = models.ForeignKey(Comment, verbose_name="댓글", on_delete=models.CASCADE, related_name='likes', null=True, blank=True)
    
    class Meta:
        unique_together = (('user', 'post'), ('user', 'comment'))  
