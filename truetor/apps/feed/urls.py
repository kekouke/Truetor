from django.urls import path
from .views import search, feed

from .api import api_add_like, api_add_tweet

urlpatterns = [
    path('search/', search, name='search'),
    path('feed/', feed, name='feed'),
    path('api/add_tweet/', api_add_tweet, name='api_add_tweet'),
    path('api/add_like/', api_add_like, name = 'api_add_like')
]