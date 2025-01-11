from django.urls import path
from .views import *

app_name = 'board'

urlpatterns=[

    # 글쓰기
    path('create', board_create, name="board_create"),

    # 디테일
    path('detail/<int:pk>', board_detail, name="board_detail"),

    # 리스트 url
    path('list', board_list, name="board_list"),

    # 글 업데이트
    path('update/<int:pk>', board_update, name="board_update"),

    # 글 삭제
    path('delete/<int:pk>', board_delete, name="board_delete"),
]