from django.shortcuts import render
from .models import Category, Blogger, Post
from django.views import generic

#Create function of main page
def index(request):
    bloggers=Blogger.objects.all()[:3]
    categories=Category.objects.all()[:3]
    posts=Post.objects.order_by('-timestamp')[:3]

    return render(request, 'index.html', context={'bloggers': bloggers, 'categories': categories, 'posts': posts})

#Create default classes view for model Blogger
class BloggerListView(generic.ListView):
    model= Blogger
    paginate_by=10
class BloggerDetailView(generic.DetailView):
    model= Blogger
#Create default classes view for model Post
class PostListView(generic.ListView):
    model= Post
    paginate_by=10
class PostDetailView(generic.DetailView):
    model=Post
#Create default classes view for model Category
class CategoryListView(generic.ListView):
    model= Category
    paginate_by=10
class CategoryDetailView(generic.DetailView):
    model=Category
    paginate_by=10

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        genre=Category.objects.get(id=self.kwargs['pk'])
        context['category_posts']= genre.category_post.all()[:10]
        return context

def search(request):
    if request == "POST":
        form= request.POST.name
        result_search_posts=Post.objects.filter(title_lower__contains= form)
        result_search_bloggers=Blogger.objects.filter(nickname_lower__contains= form)
        result_search_categories=Category.objects.filter(name_lower__contains= form)
        return render(request, 'result_search.html', context={'result_search_posts': result_search_posts, 'result_search_bloggers':result_search_bloggers, 'result_search_categories': result_search_categories})
    return render(request, 'index.html')
