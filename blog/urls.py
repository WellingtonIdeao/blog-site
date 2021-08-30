from django.urls import path
from .views import PostListView, PostDetailView, PostListByTag, \
    PostListByAuthor

app_name = 'blog'

urlpatterns = [
    path('post/', PostListView.as_view(), name='index'),
    path('post/<slug:slug>/', PostDetailView.as_view(), name='post-detail'),
    path('post/tag/<slug:slug>/', PostListByTag.as_view(), name='post_list_by_tag'),
    path('post/author/<slug:slug>/', PostListByAuthor.as_view(), name='post_list_by_author'),
]