from django.urls import path
from .views import *

app_name = 'home'

urlpatterns = [

    # 메인
    path('', main, name='main'),

]