from django.urls import path
from .views import userprofile, edit_profile, follows, followers, unfollow_user, follow_user

urlpatterns = [
    path('<str:username>/', userprofile, name='userprofile'),
    path('u/edit_profile/', edit_profile, name='edit_profile'),
    path('<str:username>/follow/', follow_user, name='follow_user'),
    path('<str:username>/unfollow/', unfollow_user, name='unfollow_user'),
    path('<str:username>/followers/', followers, name='followers'),
    path('<str:username>/follows/', follows, name='follows'),
]