from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import PublishedPost
from taggit.models import Tag


class PostListView(ListView):
    template_name = 'blog/index.html'
    context_object_name = 'post_list'
    paginate_by = 4

    def get_queryset(self):
        queryset = PublishedPost.objects.all()
        return queryset


class PostListByTag(ListView):
    template_name = 'blog/post/list_tag.html'
    context_object_name = 'post_list'
    paginate_by = 4

    def get_queryset(self):
        tag = get_object_or_404(Tag, slug=self.kwargs['slug'])
        queryset = PublishedPost.objects.filter(tags__in=[tag])
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        tag = get_object_or_404(Tag, slug=self.kwargs['slug'])
        context['tag'] = tag
        return context


class PostDetailView(DetailView):
    template_name = 'blog/post/post_detail.html'
    context_object_name = 'post'

    def get_queryset(self):
        queryset = PublishedPost.objects.all()
        return queryset
