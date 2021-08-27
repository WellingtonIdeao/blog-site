from django.test import TestCase
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse
from ..models import Post, PublishedPost


class PostListViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        n_posts = 3
        user = User.objects.create_superuser(username='admin', password='admin')
        title = 'FOO title'

        for index in range(n_posts):
            unique_title = title+str(index)
            Post.objects.create(title=unique_title,
                                slug=slugify(unique_title),
                                author=user,
                                body='FOO body',
                                status='published')

    def test_view_url_exists_at_desired_location(self):
        url = '/blog/post/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        url = reverse('blog:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_view_correct_template_used(self):
        template_name = 'blog/index.html'
        url = reverse('blog:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name)

    def test_view_context_object_name(self):
        url = reverse('blog:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue('post_list' in response.context)

    def test_view_get_queryset_published_posts(self):
        url = reverse('blog:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['post_list'].count(), 3)


class PostDetailViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_superuser(username='admin', password='admin')
        title = 'FOO title'
        Post.objects.create(title=title,
                            slug=slugify(title),
                            author=user,
                            body='FOO body',
                            status='published')

    def test_view_url_exists_at_desired_location(self):
        url = '/blog/post/foo-title/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        post = Post.objects.get(pk=1)
        url = reverse('blog:post-detail', kwargs={'slug': post.slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_view_correct_template_used(self):
        template_name = 'blog/post/post_detail.html'
        post = Post.objects.get(pk=1)
        url = reverse('blog:post-detail', kwargs={'slug': post.slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name)

    def test_view_context_object_name(self):
        post = PublishedPost.objects.get(pk=1)
        url = reverse('blog:post-detail', kwargs={'slug': post.slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue('post' in response.context)

    def test_view_get_queryset_published_post(self):
        post = PublishedPost.objects.get(pk=1)
        url = reverse('blog:post-detail', kwargs={'slug': post.slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['post'].status, 'published')
