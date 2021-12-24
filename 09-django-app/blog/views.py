from django.shortcuts import render
from .models import Post
from django.views import generic

# Create your views here.

# This class connects model to template
class BlogView(generic.DetailView):
    model = Post
    template_name = 'blog.html' # This is defined in urls.py

# Home View is static so inherits from TemplateView
class AboutView(generic.TemplateView):
    # Page doesn't need a model as is a static page
    template_name = 'about.html'

class PostList(generic.ListView):
     # ListView expects a queryset. Post here refers to Model
     # We are looking for published blog posts. Ordered by date created (the - will reverse)
    queryset = Post.objects.filter(status = 1).order_by('-date_created')
    template_name = 'index.html'
