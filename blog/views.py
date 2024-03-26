from .models import Post
from django.shortcuts import render
from django.views.generic import ListView, DetailView

# Create your views here.

class PostListView(ListView):
  model = Post
  context_object_name = 'all_post'
  template_name = 'blog/post/list.html'

class PostDetailView(DetailView):
  model = Post
  context_object_name = 'post'
  template_name = 'blog/post/detail.html'