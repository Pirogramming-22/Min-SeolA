from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

app_name = 'pirostagram'

urlpatterns = [
    path('', login, name='login'),
    path('login/', login, name='login'),
    path('signup/', signup, name='signup'),
    path('profile/', profile, name='profile'),
    path('upload/', create_post, name='create_post'),
    path('follow_toggle/', follow_toggle, name='follow_toggle'),
    path('post/<int:post_id>/', detail, name='detail'),
    path('add_comment/', add_comment, name='add_comment'),
    path('delete_comment/', delete_comment, name='delete_comment'),
    path('toggle_like/', toggle_like, name='toggle_like'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)