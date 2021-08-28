from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Post, PublishedPost


class PostListView(ListView):
    template_name = 'blog/index.html'
    context_object_name = 'post_list'
    paginate_by = 4

    def get_queryset(self):
        queryset = PublishedPost.objects.all()
        return queryset


class PostDetailView(DetailView):
    template_name = 'blog/post/post_detail.html'
    context_object_name = 'post'

    def get_queryset(self):
        queryset = PublishedPost.objects.all()
        return queryset
