from django.urls import path
from .views import PostListView

app_name = 'blog'

urlpatterns = [
    path('list/', PostListView.as_view(), name='post-list'),
]