from django.shortcuts import render, redirect
from .models import Category, Blogger, Post, Coment
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.forms import CommentForm, AboutBloggerForm, PostForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
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

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        if str(self.request.user) == "AnonymousUser":
           return context
        elif self.request.user.email == Blogger.objects.get(id= self.kwargs['pk']).email and not Blogger.objects.get(id=self.kwargs['pk']).about_blogger:
            context['Edit']= True
            context['form_edit']=AboutBloggerForm
            context['form_post']=PostForm
            return context
        elif self.request.user.email == Blogger.objects.get(id=self.kwargs['pk']).email and Blogger.objects.get(id=self.kwargs['pk']).about_blogger:
            context['Edit']= True
            context['form_edit']= AboutBloggerForm(initial={'about_blogger':Blogger.objects.get(id=self.kwargs['pk']).about_blogger})
            context['form_post']=PostForm
            return context
    def post(self, request, *args, **kwargs):
        if request.method== 'POST':
            if self.request.user.email== Blogger.objects.get(id=self.kwargs['pk']).email and request.POST.get('about_blogger'):
                blogger= Blogger.objects.get(id=self.kwargs['pk'])
                blogger.about_blogger= request.POST['about_blogger']
                blogger.save()
                return super().get(request, *args, **kwargs)
            elif self.request.user.email== Blogger.objects.get(id=self.kwargs['pk']).email and request.POST['title']:
                post=Post.objects.create(title= request.POST['title'], content = request.POST['content'], blogger= Blogger.objects.get(id=self.kwargs['pk']))
                for category in request.POST.getlist('categories'):
                    post.categories.add(category)
                
                return redirect(reverse('blogger-detail', args=[str(self.kwargs['pk'])]))
#Create default classes view for model Post
class PostListView(generic.ListView):
    model= Post
    paginate_by=10
class PostDetailView(generic.DetailView):
    model=Post
    paginate_by=10
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        get_post=Post.objects.get(id=self.kwargs['pk'])
        context['comment']=get_post.post_comment.all().order_by('-timestamp')
        context['form']= CommentForm
        return context
    def post(self, request, *args, **kwargs):
        if request.method=="POST":
            filter_user={'user_field':user for user in Blogger.objects.filter(email__exact= self.request.user.email)}
            comment_object=Coment.objects.create(title= request.POST['title'], content= request.POST['content'], post= get_object_or_404(Post, pk= self.kwargs['pk']), blogger= filter_user['user_field'])
            return redirect(reverse('post-detail', args=[str(self.kwargs['pk'])]))

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
    if request.method == "POST":
        form= request.POST
        result_search_posts=Post.objects.filter(title__icontains= form['search_field'].strip())[:10]
        result_search_bloggers=Blogger.objects.filter(nickname__icontains= form['search_field'].strip())[:10]
        find_categories=Category.objects.filter(name__icontains= form['search_field'].strip())[:10]
        preresult_posts_categories=[genre.category_post.all()[:10] for genre in find_categories]
        result_search_categories=[result for item in preresult_posts_categories for result in item]
        maximal_match=set()
       

        if not result_search_bloggers:
            pre_search_bloggers= form['search_field'].strip().split()
            pre_result_search_bloggers=[Blogger.objects.filter(nickname__icontains=item)[:10] for item in pre_search_bloggers[:10]]
            result_search_bloggers=set([result for item in pre_result_search_bloggers for result in item])

        if not result_search_posts:
            pre_search_posts= form['search_field'].strip().split()
            pre_result_search_posts=[Post.objects.filter(title__icontains=item)[:10] for item in pre_search_posts[:10]]
            result_search_posts=set()
            for item in pre_result_search_posts:
                for result in item:
                    result_search_posts.add(result)
                    if result.blogger in result_search_bloggers:
                        maximal_match.add(tuple([result.blogger, result]))

        if not result_search_categories:
            pre_search_categories= form['search_field'].strip().split()
            pre_result_search_categories=[Category.objects.filter(name__icontains=item)[:10] for item in pre_search_categories[:10]]
            find_categories_posts=[result.category_post.all()[:10] for item in pre_result_search_categories for result in item]
            result_search_categories=set()
            for item in find_categories_posts:
                for result in item:
                    result_search_categories.add(result)
                    if result in result_search_posts or result.blogger in result_search_bloggers:
                        maximal_match.add(tuple([result.blogger, result]))

        return render(request, 'result_search.html', context={'maximal_match':maximal_match,'result_search_posts': result_search_posts, 'result_search_bloggers':result_search_bloggers, 'result_search_categories': result_search_categories})
    else:
        return redirect(reverse('index'))

@login_required
def my_blog(request):
    for blogger in Blogger.objects.filter(email__exact= request.user.email):
        return redirect(reverse('blogger-detail', args=[str(blogger.id)]))
