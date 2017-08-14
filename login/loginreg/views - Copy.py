from login.settings import SENDER,PASS
import smtplib
from django.shortcuts import render,render_to_response
from django import forms
from django.views.generic import View
from django.views.generic.edit import FormView
from django.views import generic
#require a form to create a new object
from django.views.generic.edit import CreateView,UpdateView ,DeleteView
# for uploading form
from django.core.urlresolvers import reverse_lazy
# for login
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.views.generic import View
from .forms import UserForm ,UserFormlog
from django.template import RequestContext
from django.contrib.auth import views as auth_views
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.

def create_profile(request):
    if request.method == 'GET':
          user_form = UserForm
          return render(request, 'profile.html', {
        'user_form': user_form
    })

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid() :
           user1= user_form.save(commit=False)
           #prof= profile_form.save()
           username = user_form.cleaned_data['username']
           fname = user_form.cleaned_data['first_name']
           password = user_form.cleaned_data['password']
           email = user_form.cleaned_data['email']
           user1.set_password(password)
           user1.save()
           msg="Hello , \n Welcome here"
           smtp= smtplib.SMTP('smtp.gmail.com')
           smtp.ehlo()
           smtp.starttls()
           smtp.ehlo()
           smtp.login(SENDER,PASS)
           smtp.sendmail(SENDER,email,msg)
           smtp.quit()
           #profile=profile_form.save(commit=False)
           #profile.user_id=user1.id+1
           #profile.college=profile_form.cleaned_data['college']
           #profile.save()
         
           user = authenticate(username=username ,password=password)

           if user is not None:

                if user.is_active:
                      login(request, user)
                      return redirect('index.html')
                      #return render(request,'index.html'

           #profile_form.save()
            #return redirect('settings:profile')
    return render(request, 'register/profile.html', {
        'user_form': user_form 
    })


def indexpage(request):
    if request.method == 'GET':
          user_form = UserForm
          return render(request, 'index.html', )
       
global user_form1

#@login_required  for stopping user from some pages
def userlogin(request):
    ab="pagal hai"
    if request.method == 'GET':
          user_form = UserFormlog
          return render(request, 'login.html', {
        'form': user_form    #user_form
    })

    if request.method == 'POST':
        user_form1 = UserFormlog(request.POST)
        if user_form1.is_valid() :
           ab="post chala"       
     
           #prof= profile_form.save()
           username = user_form1.cleaned_data['username']
           password = user_form1.cleaned_data['password']
           #profile=profile_form.save(commit=False)
           #profile.user_id=user1.id+1
           #profile.college=profile_form.cleaned_data['college']
           #profile.save()
         
           user1 = authenticate(username=username ,password=password)

           if user1 :
                auth.login(request, user1)
                #return redirect('index.html')
                return render(request,'index.html',{ 'user1': user_form1 })
           else:
                return redirect('nope.html')
           #profile_form.save()
            #return redirect('settings:profile')
        else:
            print user_form1.errors
        
    return render(request, 'login.html', {
        'user_form': user_form1 ,'ab':ab
    })

def logout(request):
    auth.logout(request)
    #user_form1= users.objects.filter(user__username=request.user)
    user_form1=request.user
    user_form1.username=''
    return render_to_response('login.html', {'box_width': '402',
                    'logged_out': '1',})
                             # context_instance=RequestContext(request))

