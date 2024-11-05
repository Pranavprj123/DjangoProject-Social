from django.shortcuts import render
# Create your views here.
from .forms import *


def user_login(request):
    context = {
        'form':LoginForm,
        'title':'Login'
    }

    return render(request,'forms.html',context)


def register(request):
    context = {
        'form':RegisterForm(),
        'userform': UserForm,
        'title':'Register',
    }

    return render(request,'forms.html',context)

from .models import Post
def posts(request):
    context = {
        'posts':Post.objects.all()
    }

    return render(request,'post.html',context)


def create_post(request):
    context = {
        'forms':PostForm(),
        'title':'Post'
    }
    return render(request,'forms.html',context)

