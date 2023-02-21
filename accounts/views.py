from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import SignUpForm
from blog.models import Blogger
#Create function for signup user
def SignUp(request):
    if request.method == 'POST':
        form= SignUpForm(request.POST)
        if form.is_valid():
            User.objects.create_user(username=form.cleaned_data['username'], password= form.cleaned_data['password'], email= form.cleaned_data['email'])
            Blogger.objects.create(nickname=form.cleaned_data['nickname'], email=form.cleaned_data['email'])
            return HttpResponseRedirect(reverse('login'))
        return render(request, 'accounts/signup.html', {'form':form})
    else:
        form= SignUpForm()
        return render(request, 'accounts/signup.html', {'form': form})

