from django.urls import path
from .views import userprofile, edit_profile, follows, followers, unfollow_user, follow_user

urlpatterns = [
    path('', userprofile, name='userprofile'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('follow/', follow_user, name='follow_user'),
    path('unfollow/', unfollow_user, name='unfollow_user'),
    path('followers/', followers, name='followers'),
    path('follows/', follows, name='follows'),
]