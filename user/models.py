from django.db import models
from django.contrib.auth.models import User

class Profiles(models.Model):
  user = models.OneToOneField(User,on_delete=models.CASCADE)
  bio = models.TextField()
  profile_pic = models.ImageField(default='default.jpg',upload_to='profile_pic/')