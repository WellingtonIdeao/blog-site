from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Post, PublishedPost


class PostListView(ListView):
    model = Post
    template_name = 'blog/list.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        return PublishedPost.objects.all()
