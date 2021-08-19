from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Post, PublishedPost


class PostListView(ListView):
    model = Post
    template_name = 'blog/post/list.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        return PublishedPost.objects.all()


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post/detail.html'
    context_object_name = 'post'
