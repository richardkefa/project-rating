from django.db import models
from django.contrib.auth.models import User

class Contact_info(models.Model):
  tel_number = models.IntegerField()
  github_u = models.CharField(max_length=100,null=True)
  facebook_u = models.CharField(max_length=100,null=True)
  instagram_u = models.CharField(max_length=100,null=True)
  twiter_u = models.CharField(max_length=100,null=True)
  linkedin_u = models.CharField(max_length=100,null=True)


class Profiles(models.Model):
  user = models.OneToOneField(User,on_delete=models.CASCADE)
  bio = models.TextField()
  profile_pic = models.ImageField(default='default.jpg',upload_to='profile_pic/')
  contact_info = models.OneToOneField(Contact_info,on_delete=models.CASCADE)