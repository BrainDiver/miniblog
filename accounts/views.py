from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import SignUpForm

#Create function for signup user
def SignUp(request):
    if request.method == 'POST':
        form= SignUpForm(request.POST)
        if form.is_valid():
            User.objects.create_user()
        return HttpResponseRedirect('SignUp_Confirm')
    else:
        form= SignUpForm()
        return render(request, 'accounts/signup.html', context= {'form': form})
