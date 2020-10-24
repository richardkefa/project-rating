from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserRegistrationForm,UserUpdateForm,ProfileUpdateForm,ContactUpdateForm

def register(request):
  if request.method == 'POST':
    form = UserRegistrationForm(request.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data.get('username')
      messages.success(request,f'Your account has been created successfuly')
      return redirect('login')
  else:
    form = UserRegistrationForm()
    
  return render(request,'user/register.html',{"form":form})

def profile(request):
  if request.method == 'POST':
    u_form = UserUpdateForm(request.POST,instance=request.user)
    p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profiles)
    c_form = ContactUpdateForm(request.POST,instance=request.user.contact_info)
    
    if u_form.is_valid() and p_form.is_valid() and c_form.is_valid():
      u_form.save()
      p_form.save()
      c_form.save()
      
      messages.success(request,f'Profile and Contact info updated successfuly')
      return redirect('profile')
  else:
    u_form = UserUpdateForm(instance=request.user)
    p_form = ProfileUpdateForm(instance=request.user.profiles)
    c_form = ContactUpdateForm(instance=request.user.contact_info)
  context ={
    "u_form":u_form,
    "p_form":p_form,
    "c_form":c_form,
  }
  
  return render(request,'user/profile.html',context)
