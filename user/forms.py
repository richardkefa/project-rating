from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profiles,Contact_info

class UserRegistrationForm(UserCreationForm):
  email = forms.EmailField()
  
  class Meta:
    model = User
    fields = ['username','email','password1','password2',]
    
class UserUpdateForm(forms.ModelForm):
  email = forms.EmailField()
  
  class Meta:
    model = User
    fields =['username','email']
    
class ProfileUpdateForm(forms.ModelForm):
  
  class Meta:
    model = Profiles
    fields =['profile_pic','bio']

class ContactUpdateForm(forms.ModelForm):
  
  class Meta:
    model = Contact_info
    
    fields = [
      'tel_number',
      'github_u',
      'facebook_u',
      'instagram_u',
      'twiter_u',
      'linkedin_u',
      ]