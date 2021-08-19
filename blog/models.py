from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')


class Post(models.Model):
    # objects = models.Manager()  # The default manager.
    # published = PublishedManager()  # Custom manager.

    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    author = models.ForeignKey(User,
                               related_name='blog_posts',
                               related_query_name='post',
                               on_delete=models.CASCADE)

    body = models.TextField()

    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')

    class Meta:
        ordering = ('-publish', )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post-detail', kwargs={'slug': self.slug})


class PublishedPost(Post):
    objects = PublishedManager()  # default Custom manager

    class Meta:
        proxy = True
