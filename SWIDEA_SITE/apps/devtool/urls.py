from django.urls import path
from . import views

app_name='devtool'

urlpatterns = [
    path('create/', views.create, name='create'),
    path('list/', views.list, name='list'),
    path('detail/<int:pk>/', views.detail, name='detail'),
    path('update/<int:pk>', views.update, name='update'),
    path('delete/<int:pk>', views.delete, name='delete'),
]
