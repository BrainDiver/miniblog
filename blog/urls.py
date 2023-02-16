from django.urls import path, re_path
from . import views 

urlpatterns =[
    path("", views.index, name='index'),
    re_path(r'^bloggers/$', views.BloggerListView.as_view(), name='bloggers'),
    re_path(r'^posts/$', views.PostListView.as_view(), name= 'posts'),
    re_path(r'^categories/$', views.CategoryListView.as_view(), name='categories'), 
]
