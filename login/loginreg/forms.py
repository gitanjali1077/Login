from django.contrib.auth.models import User
from django import forms
from django.db import models
#from .models import newuser
from captcha.fields import CaptchaField

class UserForm(forms.ModelForm):
   password = forms.CharField(widget=forms.PasswordInput)

   class Meta:

       model = User
       fields=['username','first_name','email','password']

    

class UserFormlog(forms.Form):
    username= forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    captcha = CaptchaField()

#  no need of meta class
   # class Meta:
   #     #contain info about this outer class
    #    model = User
    #    fields = ['username','password',]
