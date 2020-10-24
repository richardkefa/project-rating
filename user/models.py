from django.db import models
from django.contrib.auth.models import User


class Profiles(models.Model):
  user = models.OneToOneField(User,on_delete=models.CASCADE)
  bio = models.TextField()
  profile_pic = models.ImageField(default='default.jpg',upload_to='profile_pic/')
  
  def __str__(self):
    return f'{self.user.username} Profiles'
  
class Contact_info(models.Model):
  user = models.OneToOneField(User,on_delete=models.CASCADE, default=0)
  tel_number = models.CharField(max_length=20)
  github_u = models.CharField(max_length=100,null=True)
  facebook_u = models.CharField(max_length=100,null=True)
  instagram_u = models.CharField(max_length=100,null=True)
  twiter_u = models.CharField(max_length=100,null=True)
  linkedin_u = models.CharField(max_length=100,null=True)
  
  def __str__(self):
    return self.tel_number