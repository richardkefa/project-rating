from django.db import models
from datetime import dt
from django.contrib.auth.models import User
from django.urls import reverse 

class Projects(models.Model):
  project_title = models.CharField(max_length=100)
  landing_page_image = models.ImageField(upload_to='images/')
  description = models.TextField()
  repo_link = models.CharField(max_length=200)
  live_link = models.CharField(max_length=500)
  user = models.ForeignKey(User,on_delete=models.CASCADE,default='1')
  


