from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse 

class Projects(models.Model):
  project_title = models.CharField(max_length=100)
  landing_page_image = models.ImageField(upload_to='images/')
  description = models.TextField()
  repo_link = models.CharField(max_length=200)
  live_link = models.CharField(max_length=500)
  user = models.ForeignKey(User,on_delete=models.CASCADE,default='1')
  post_date =  models.DateField(auto_now_add=True)
  
  def __str__(self):
    return self.project_title
  @classmethod
  def search_by_titles(cls,search):
    
    projects = cls.objects.filter(project_title__icontains=search_term)
    return projects
  
  def get_absolute_url(self):
    return reverse('project_detail',kwargs={'pk':self.pk})
  
class Ratings(models.Model):
  project = models.ForeignKey(Projects,on_delete=models.CASCADE,default='1')
  design = models.IntegerField(default=0)
  usability = models.IntegerField(default=0)
  content = models.IntegerField(default=0)