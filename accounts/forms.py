from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from blog.models import Blogger, Coment, Post, Category
from django.forms import ModelForm
import datetime

class SignUpForm(forms.Form):
    username= forms.CharField(max_length=20, required=True, help_text='Create Username')
    password = forms.CharField(max_length=20, required=True, widget=forms.PasswordInput(attrs={
        'class': 'input-text with-border', 'placeholder': 'Password'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'input-text with-border', 'placeholder': 'Repeat Password'}))
    email= forms.EmailField(max_length= 200, required= True, help_text='Enter your email')
    nickname= forms.CharField(max_length=20, required= True, help_text= "Enter nickname you want")
    def clean_confirm_password(self):
        data = {'password':self.cleaned_data['password'], 'confirm_password':self.cleaned_data['confirm_password']}
        if data['password'] != data['confirm_password']:
            raise forms.ValidationError(_('passwords didnt match'))
        return data
    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.filter(email=data):
            raise forms.ValidationError(_('email already registered'))
        return data

    def clean_nickname(self):
        data= self.cleaned_data['nickname']
        if Blogger.objects.filter(nickname=data):
            raise forms.ValidationError(_('nickname already taken'))
        return data

class CommentForm(forms.ModelForm):
    class Meta:
        model=Coment
        fields=['title', 'content']

class AboutBloggerForm(forms.ModelForm):
    class Meta:
        model=Blogger
        fields=['about_blogger',]

DISPLAY_CHOICES = (
    ("locationbox", "Display Location"),
    ("displaybox", "Display Direction")
)

class PostForm(forms.ModelForm):
    categories= forms.ModelMultipleChoiceField(queryset=Category.objects.all(), widget=forms.CheckboxSelectMultiple(),)
    class Meta:
        model=Post
        fields=['title', 'content', 'categories']

