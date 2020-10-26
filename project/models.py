from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse 
from cloudinary.models import CloudinaryField


class Projects(models.Model):
  project_title = models.CharField(max_length=100)
  landing_page_image = CloudinaryField('image')
  description = models.TextField()
  repo_link = models.CharField(max_length=200)
  live_link = models.CharField(max_length=500)
  user = models.ForeignKey(User,on_delete=models.CASCADE,default='1')
  post_date =  models.DateField(auto_now_add=True)
  
  def __str__(self):
    return self.project_title
  
  @classmethod
  def search_by_titles(cls,search_term):
    
    projects = cls.objects.filter(project_title__icontains=search_term)
    return projects
  
  def get_absolute_url(self):
    return reverse('project_detail',kwargs={'pk':self.pk})
  
RATE_CHOICES=[
  (1,'1'),
  (2,'2'),
  (1,'3'),
  (1,'4'),
  (1,'5'),
  (1,'6'),
  (1,'7'),
  (1,'8'),
  (1,'9'),
  (1,'10'),
]  
class Ratings(models.Model):
  project = models.ForeignKey(Projects,on_delete=models.CASCADE,default='1')
  design = models.PositiveIntegerField(choices=RATE_CHOICES)
  usability = models.PositiveIntegerField(choices=RATE_CHOICES)
  content = models.PositiveIntegerField(choices=RATE_CHOICES)
  comment = models.TextField(blank=True)
  user = models.ForeignKey(User,on_delete=models.CASCADE,default="1")
  
  def __str__(self):
    return self.user.username