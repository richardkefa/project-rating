from django.conf.urls import  url
from . import views
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  url(r'^$',PostListView.as_view(),name='home'),
  url(r'^project/(?P<pk>\d+)/$',PostDetailView.as_view(),name='project_detail'),
  url(r'^project/new/$',PostCreateView.as_view(),name='project_create'),
  url(r'^project/(?P<pk>\d+)/update/$',PostUpdateView.as_view(),name='project_update'),
  url(r'^project/(?P<pk>\d+)/delete/$',PostDeleteView.as_view(),name='project_delete'),
  url(r'^search/', views.search_results, name='search_results'),
  url(r'^project/(?P<pk>\d+)/rate/$',views.Rating,name='project_rating'),  
]

if settings.DEBUG:
  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)