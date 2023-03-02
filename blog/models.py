from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Category(models.Model):
    """
    Model representing an category.
    """
    name = models.CharField(max_length=20, help_text= "Enter a blog category")
    class Meta:
        ordering=['name']
    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.name
    def get_absolute_url(self):
        return reverse('category-detail', args=[str(self.id)])
class Blogger(models.Model):
    """
    Model representing an blogger.
    """
    nickname = models.CharField(max_length=200)
    email = models.EmailField(unique= True)
    date_of_birth = models.DateField(null= True, blank= True)
    about_blogger = models.TextField(max_length= 3000, help_text= 'information about bloger')
    class Meta:
        ordering=['nickname']
    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.nickname

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.
        """
        return reverse('blogger-detail', args=[str(self.id)])

class Post(models.Model):
    title=models.CharField(max_length=40, help_text='Enter title for this post')
    blogger=models.ForeignKey('Blogger', on_delete=models.CASCADE,related_name= "bloggerposts")
    categories=models.ManyToManyField(Category, related_name='category_post')
    content=models.TextField()
    timestamp=models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering=['-timestamp']
    def __str__(self):
        return self.title
    def display_category(self):
        return ", ".join([categories.name for categories in self.categories.all()[:3]])
    def get_absolute_url(self):
        return reverse('post-detail', args=[str(self.id)])

class Coment(models.Model):
    title=models.CharField(max_length= 20, help_text="Enter coment title")
    content=models.TextField(null=True, blank=True)
    timestamp=models.DateTimeField(auto_now_add=True)
    post= models.ForeignKey('Post', on_delete=models.CASCADE, related_name='post_comment')
    blogger= models.ForeignKey('Blogger', on_delete=models.CASCADE, related_name= 'blogger_coments')

    def __str__(self):
        return self.title
