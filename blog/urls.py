from django.urls import path
from .views import PostListView, PostDetailView

app_name = 'blog'

urlpatterns = [
    path('post/', PostListView.as_view(), name='post-list'),
    path('post/<slug:slug>/', PostDetailView.as_view(), name='post-detail'),
]