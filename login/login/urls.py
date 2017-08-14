"""login URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from loginreg.views import create_profile,indexpage,userlogin,logout
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
       url(r'^register/$', create_profile , name='index'),
   url(r'^register/index.html/$', indexpage , name='index1'),
       url(r'^login/$', userlogin, name='login'),
#url(r'^', include('django.contrib.auth.urls')),
    url(r'^login/reset/$',auth_views.password_reset, {'post_reset_redirect' : '/login/reset/done/'}, name='forgot'),
#  url(r'^', include('django.contrib.auth.urls')),
  
  url(r'^login/reset/done/$',
        auth_views.password_reset_done),
   url(r'^login/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 
      auth_views.password_reset_confirm, 
        {'post_reset_redirect' : 'login/done/'},name='password_reset_confirm'),
    url(r'^login/done/$', 
        auth_views.password_reset_complete),
    
     
url(r'^login/index.html/$', indexpage , name='index1'),
   url(r'^logout/$',logout ,   name='logout'),
      url(r'^captcha/', include('captcha.urls')),


    #auth_views.logout     {'next_page': '/login'},    auth_views.login   {'template_name': 'login.html'},
]
