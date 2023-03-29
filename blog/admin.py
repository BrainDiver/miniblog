from django.contrib import admin
from .models import Category, Blogger, Post, Coment
from typing import Set

from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

#register model Category
admin.site.register(Category)

#making Post inline class
class PostInline(admin.StackedInline):
    model=Post
#register model Blogger
@admin.register(Blogger)
class BloggerAdmin(admin.ModelAdmin):
    list_display=('nickname', 'email', 'date_of_birth', 'id')
    fields=['nickname', ('email', 'date_of_birth', 'about_blogger')]
    inlines=[PostInline]
#register model Post
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=('title', 'blogger', 'display_category', 'timestamp')
    list_filtet=('blogger', 'categories','timestamp', 'title')
#unregister default User model
admin.site.unregister(User)
#register custom User model
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser
        disabled_fields = set()  # type: Set[str]

        if not is_superuser:
            disabled_fields |= {
                'username',
                'is_superuser',
                'user_permissions',
            }

        # Prevent non-superusers from editing their own permissions
        if (
            not is_superuser
            and obj is not None
            and obj == request.user
        ):
            disabled_fields |= {
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions',
            }

        for f in disabled_fields:
            if f in form.base_fields:
                form.base_fields[f].disabled = True

        return form

admin.site.register(Coment)
