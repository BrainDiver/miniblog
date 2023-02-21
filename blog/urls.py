from django.urls import path, re_path
from . import views 

urlpatterns =[
    path("", views.index, name='index'),
    re_path(r'^bloggers/$', views.BloggerListView.as_view(), name='bloggers'),
    re_path(r'^bloggers/(?P<pk>\d+)$', views.BloggerDetailView.as_view(), name='blogger-detail'),
    re_path(r'^posts/$', views.PostListView.as_view(), name= 'posts'),
    re_path(r'^posts/(?P<pk>\d+)$', views.PostDetailView.as_view(), name='post-detail'),
    re_path(r'^categories/$', views.CategoryListView.as_view(), name='categories'), 
    re_path(r'^categories/(?P<pk>\d+$)', views.CategoryDetailView.as_view(), name='category-detail'),
    path("search", views.search, name='search')
]
