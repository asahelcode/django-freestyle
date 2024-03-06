from django.shortcuts import render, get_object_or_404
from .models import Post
from django.http import Http404

# Create your views here.
def post_list(request):
  published_posts = Post.published.all()
  return render(request, 'blog/post/post_list.html', { 'posts': published_posts })

def post_detail(request, id):
  post = get_object_or_404(Post, id, Post.Status.PUBLISHED)
  return render(request, 'blog/post/post_detail.html', { 'post': post })