from django.urls import path
from . import views

app_name = 'idealist'

urlpatterns = [
    path('', views.list, name='list'),
    path('idealist/create/', views.create, name='create'),  
    path('idealist/list/', views.list, name='list'), 
    path('idealist/detail/<int:pk>/', views.detail, name='detail'),  
    path('idealist/update/<int:pk>/', views.update, name='update'), 
    path('idealist/delete/<int:pk>/', views.delete, name='delete'),  
    path('idealist/update_interest/<int:pk>/<str:action>/', views.update_interest, name='update_interest'), 
    path('idealist/startoggle/<int:idea_id>/', views.startoggle, name='startoggle'),
    path('detail/<int:id>/', views.devtool_detail, name='devtool_detail'),
]
