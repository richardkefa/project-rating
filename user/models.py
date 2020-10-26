from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField



class Profiles(models.Model):
  user = models.OneToOneField(User,on_delete=models.CASCADE)
  bio = models.TextField()
  profile_pic = CloudinaryField('image')
  
  def __str__(self):
    return "{}-{}-{}".format(self.user,self.bio,self.profile_pic)
  
class Contact_info(models.Model):
  user = models.OneToOneField(User,on_delete=models.CASCADE, default=0)
  tel_number = models.CharField(max_length=20)
  github_u = models.CharField(max_length=100,blank=True)
  facebook_u = models.CharField(max_length=100,blank=True)
  instagram_u = models.CharField(max_length=100,blank=True)
  twiter_u = models.CharField(max_length=100,blank=True)
  linkedin_u = models.CharField(max_length=100,blank=True)
  
  def __str__(self):
    return "{}-{}-{}-{}-{}-{}-{}".format(self.tel_number,self.github_u,self.facebook_u,self.twiter_u,self.linkedin_u,self.instagram_u,self.user)