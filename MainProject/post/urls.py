from django.urls import path
from . import views

urlpatterns= [
    path('login/',views.user_login,name='login'),
    path('register/',views.register,name='register'),
    path('posts/',views.posts,name='posts'),
    path('create-post/',views.create_post,name='create_post'),
]