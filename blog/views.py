from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Post, PublishedPost


class PostListView(ListView):
    template_name = 'blog/post/list.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        queryset = PublishedPost.objects.all()
        return queryset


class PostDetailView(DetailView):
    template_name = 'blog/post/detail.html'
    context_object_name = 'post'

    def get_queryset(self):
        queryset = PublishedPost.objects.all()
        return queryset
