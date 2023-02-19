from django import forms
from django.core.exceptions import ValidationError

class SignUpForm(forms.Form):
    username= forms.CharField(max_length=20, required=True, help_text='Create Username')
    password= forms.CharField(max_length=20, required=True, help_text= 'Create Password')
    confirm_password= forms.CharField(max_length=20, required=True, help_text= 'Repeat Password')

