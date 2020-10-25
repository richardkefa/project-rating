from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import Projects,Ratings
from django.views.generic import ListView,CreateView,UpdateView,DetailView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

class PostListView(ListView):
  model = Projects
  template_name = 'project/home.html'
  context_object_name = 'projects'
  ordering = ['-post_date']
  
class PostDetailView(DetailView):
  model = Projects
  template_name = 'project/project_detail.html'
  context_object_name = 'project'
  
class PostCreateView(CreateView):
  model = Projects
  fields = ['project_title','landing_page_image','description','repo_link','live_link']
  
  def form_valid(self,form):
    form.instance.user = self.request.user
    return super().form_valid(form)
  
class PostUpdateView(UserPassesTestMixin,UpdateView):
  model = Projects
  fields = ['project_title','landing_page_image','description','repo_link','live_link']
  
  def form_valid(self,form):
    form.instance.user = self.request.user
    return super().form_valid(form)
  
  def test_func(self):
    project = self.get_object()
    if self.request.user == project.user:
      return True
    return False

  
