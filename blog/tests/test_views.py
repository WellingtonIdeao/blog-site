from django.test import TestCase
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse
from ..models import Post


class PostListViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_superuser(username='admin', password='admin')
        title = 'FOO title'
        Post.objects.create(title=title,
                            slug=slugify(title),
                            author=user,
                            body='FOO body')

    def test_view_url_exists_at_desired_location(self):
        url = '/blog/post/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        url = reverse('blog:post-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_view_correct_template_used(self):
        template_name = 'blog/post/list.html'
        url = reverse('blog:post-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name)

    def test_view_context_object_name(self):
        url = reverse('blog:post-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue('post_list' in response.context)

    def test_view_list_post(self):
        post = Post.objects.get(pk=1)
        print(post)
        url = reverse('blog:post-list')
        url2 = '/blog/post/'
        print(url)
        response = self.client.get(url2)
        length = response.context['object_list']
        print(response.context)
        self.assertTrue(len(response.context['object_list']) == 0)


class PostDetailViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_superuser(username='admin', password='admin')
        title = 'FOO title'
        Post.objects.create(title=title,
                            slug=slugify(title),
                            author=user,
                            body='FOO body')

    def test_view_url_exists_at_desired_location(self):
        post = Post.objects.get(pk=1)
        url = reverse('blog:post-detail', kwargs={'slug': post.slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
