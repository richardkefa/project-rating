from django.conf.urls import  url
from . import views
from .views import PostListView,PostDetailView,PostCreateView

urlpatterns = [
  url(r'^$',PostListView.as_view(),name='home'),
  url(r'^project/(?P<pk>\d+)/$',PostDetailView.as_view(),name='project_detail'),
  url(r'^project/new/$',PostCreateView.as_view(),name='project_create')

]