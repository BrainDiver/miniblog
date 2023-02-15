from django.contrib import admin
from .models import Category, Blogger, Post

#register model Category
admin.site.register(Category)

#making Post inline class
class PostInline(admin.StackedInline):
    model=Post
#register model Blogger
@admin.register(Blogger)
class BloggerAdmin(admin.ModelAdmin):
    list_display=('nickname', 'email', 'date_of_birth')
    fields=['nickname', ('email', 'date_of_birth')]
    inlines=[PostInline]
#register model Post
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=('title', 'blogger', 'display_category', 'timestamp')
    list_filtet=('blogger', 'display_category','timestamp', 'title')
