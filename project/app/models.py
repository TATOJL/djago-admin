from django.db import models
from django.utils import timezone
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# 景點位置
class Location(models.Model):
    name = models.CharField(max_length=255)  #位置名稱
#景點貼文
class Post(models.Model):
    subject = models.CharField(max_length=255)  #標題
    content = models.CharField(max_length=255)  #內容
    author = models.CharField(max_length=20)  #貼文者
    create_date = models.DateField(default=timezone.now)  #貼文時間
    location = models.ForeignKey(Location, on_delete=models.CASCADE) #景點位置
# Create your models here.
class Expense(models.Model):
    name = models.CharField(max_length=255)  #花費項目
    price = models.IntegerField() #金額

class RegisterForm(UserCreationForm):
    username = forms.CharField(
        label="帳號",
        widget=forms.TextInput(attrs={'class': 'form-control'})
        
    )
    email = forms.EmailField(
        label="電子郵件",
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    password1 = forms.CharField(
        label="密碼",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    password2 = forms.CharField(
        label="密碼確認",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class UpdateForm(UserCreationForm):
    email = forms.EmailField(
        label="電子郵件",
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    password1 = forms.CharField(
        label="更改密碼",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    password2 = forms.CharField(
        label="密碼確認",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    class Meta:
        model = User
        fields = ( 'email', 'password1', 'password2')