from django.forms import ModelForm
from .models import *
from django import forms

class UserForm(ModelForm):
    password = forms.CharField(max_length=30,widget=forms.PasswordInput)
    confirm_password = forms.CharField(max_length=30,widget=forms.PasswordInput)
    class Meta:
        model = User
        fields=['username','first_name','last_name','email',]

class RegisterForm(ModelForm):
    class Meta:
        model = Person 
        exclude = ['user',]

class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30,widget=forms.PasswordInput)

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'