from django.urls import path
from .views import frontpage, signup

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('sign_up/', signup, name='sign_up'),
]