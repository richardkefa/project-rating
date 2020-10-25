from django.conf.urls import  url
from . import views
from .views import PostListView,PostDetailView

urlpatterns = [
  url(r'^$',PostListView.as_view(),name='home'),
  url(r'^project/(?P<pk>\d+)/$',PostDetailView.as_view(),name='project_detail')
]