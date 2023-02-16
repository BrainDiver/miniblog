from django.shortcuts import render
from .models import Category, Blogger, Post
from django.views import generic

#Create function of main page
def index(request):
    bloggers=Blogger.objects.all()[:3]
    categories=Category.objects.all()[:3]
    posts=Post.objects.order_by('-timestamp')[:3]

    return render(request, 'index.html', context={'bloggers': bloggers, 'categories': categories, 'posts': posts})

#Create default class view for model Blogger
class BloggerListView(generic.ListView):
    model= Blogger
    paginate_by=10

#Create default class view for model Post
class PostListView(generic.ListView):
    model= Post
    paginate_by=10

#Create default class view for model Category
class CategoryListView(generic.ListView):
    model= Category
    paginate_by=10
