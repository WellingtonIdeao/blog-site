from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import PublishedPost, Profile
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


class PostListByAuthor(ListView):
    template_name = 'blog/post/list_author.html'
    context_object_name = 'post_list'
    paginate_by = 4

    def get_queryset(self):
        """
            Get user profile that given slug from url and
            Filter queryset with post published by profile.user
        """
        profile = get_object_or_404(Profile, slug=self.kwargs['slug'])
        queryset = PublishedPost.objects.filter(author=profile.user)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = get_object_or_404(Profile, slug=self.kwargs['slug'])
        context['user'] = profile.user
        return context


class PostDetailView(DetailView):
    template_name = 'blog/post/post_detail.html'
    context_object_name = 'post'

    def get_queryset(self):
        queryset = PublishedPost.objects.all()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = super().get_object()
        profile = get_object_or_404(Profile, user=post.author)
        context['profile'] = profile
        return context
