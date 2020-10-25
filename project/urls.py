from django.conf.urls import  url
from . import views
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView

urlpatterns = [
  url(r'^$',PostListView.as_view(),name='home'),
  url(r'^project/(?P<pk>\d+)/$',PostDetailView.as_view(),name='project_detail'),
  url(r'^project/new/$',PostCreateView.as_view(),name='project_create'),
  url(r'^project/(?P<pk>\d+)/update/$',PostUpdateView.as_view(),name='project_update'),
  url(r'^project/(?P<pk>\d+)/delete/$',PostDeleteView.as_view(),name='project_delete'),

  
]