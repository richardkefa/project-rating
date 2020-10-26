from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import Projects,Ratings
from django.views.generic import ListView,CreateView,UpdateView,DetailView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .forms import RatingsForm
from cloudinary.forms import cl_init_js_callbacks      


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

  
class PostDeleteView(UserPassesTestMixin,DeleteView):
  model = Projects
  success_url = '/'
  def test_func(self):
    project = self.get_object()
    if self.request.user == project.user:
      return True
    return False
  
def search_results(request):
  
  if 'project' in request.GET and request.GET["project"]:
    search_term = request.GET.get("project")
    searched_project = Projects.search_by_titles(search_term)
    message = f"{search_term}"
    
    return render(request, 'project/search.html',{"message":message,"projects":searched_project})
  else:
    
    message ="You havent serched any term"
    return render(request, 'project/search.html',{"message":message}) 
  
  
def Rating(request,pk):
  project = Projects.objects.get(pk=pk)
  user = request.user
  ratings = Ratings.objects.filter(pk=pk)
  
  if request.method =='POST':
    form = RatingsForm(request.POST)
    if form.is_valid():
      rate = form.save(commit=False)
      rate.user = user
      rate.project = project
      rate.save()
      return render(request,'project/project_detail.html',{'ratings':ratings})
  else:
    form = RatingsForm()
  return render(request,'project/rating.html',{'project':project,'user':user,'form':form})
      