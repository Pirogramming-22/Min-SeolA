from django.contrib import admin
from .models import Post

admin.site.register(Post)
# 관리자 페이지에서 만든 모델을 보기 위해 모델을 등록함 