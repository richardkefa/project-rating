from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns=[
  url('^newuser/',views.register,name='register'),
  url('^login/',auth_views.LoginView.as_view(template_name='user/login.html'),name='login'),
  url('^logout',auth_views.LogoutView.as_view(template_name='user/logouthtml'),name='logout'),
  
]