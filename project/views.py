from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import Projects,Ratings
from django.views.generic import ListView,CreateView,UpdateView,DetailView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

class PostListView(ListView):
  model = Projects
  template_name = 'project/home.html'
  context_object_name = 'projects'
  