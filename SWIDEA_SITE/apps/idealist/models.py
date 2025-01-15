from django.db import models
from django.utils import timezone  # timezone 임포트 추가
from apps.devtool.models import DevTool

class Idea(models.Model):
    title = models.CharField('제목', max_length=50)
    image = models.ImageField('이미지', blank=True, upload_to='ideas/%Y%m%d')
    content = models.TextField('설명')
    interest = models.IntegerField('아이디어 관심도', default=0)
    devtool = models.ForeignKey(DevTool, verbose_name='개발툴', on_delete=models.CASCADE)
    star = models.BooleanField("찜하기", default=False)