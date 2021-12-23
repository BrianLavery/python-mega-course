from django.shortcuts import render
from .models import Post
from django.views import generic

# Create your views here.

# This class connects model to template
class BlogView(generic.DetailView):
    model = Post
    template_name = 'blog.html'