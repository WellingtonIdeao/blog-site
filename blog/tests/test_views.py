from django.test import TestCase
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse
from ..models import Post, PublishedPost, Profile
from taggit.models import Tag


class PostListViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        n_posts = 5
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
        self.assertEqual(response.context['post_list'].count(), 4)

    def test_view_pagination_is_four(self):
        url = reverse('blog:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertEqual(response.context['is_paginated'], True)
        self.assertTrue('page_obj' in response.context)
        self.assertTrue('paginator' in response.context)
        self.assertEqual(response.context['post_list'].count(), 4)

    def test_view_lists_all_posts(self):
        # Get second page and confirm it has (exactly) remaining 1 items
        url = reverse('blog:index')
        response = self.client.get(url, data={'page': 2})
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertEqual(response.context['is_paginated'], True)
        self.assertTrue('page_obj' in response.context)
        self.assertTrue('paginator' in response.context)
        self.assertEqual(response.context['post_list'].count(), 1)


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
        Profile.objects.create(user=user, slug=slugify(user.username))

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

    def test_view_get_context_object_names(self):
        post = PublishedPost.objects.get(pk=1)
        url = reverse('blog:post-detail', kwargs={'slug': post.slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue('post' in response.context)
        self.assertTrue('profile' in response.context)


class PostListByTagTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        n_posts = 5
        user = User.objects.create_superuser(username='admin', password='admin')
        title = 'FOO title'

        for index in range(n_posts):
            unique_title = title + str(index)
            post = Post.objects.create(title=unique_title,
                                       slug=slugify(unique_title),
                                       author=user,
                                       body='FOO body',
                                       status='published')
            post.tags.add('test')

    def test_view_url_exists_at_desired_location(self):
        url = '/blog/post/tag/test/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        tag = Tag.objects.get(pk=1)
        url = reverse('blog:post_list_by_tag', kwargs={'slug': tag.slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_view_correct_template_used(self):
        template_name = 'blog/post/list_tag.html'
        tag = Tag.objects.get(pk=1)
        url = reverse('blog:post_list_by_tag', kwargs={'slug': tag.slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name)

    def test_view_context_object_names(self):
        tag = Tag.objects.get(pk=1)
        url = reverse('blog:post_list_by_tag', kwargs={'slug': tag.slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue('post_list' in response.context)
        self.assertTrue('tag' in response.context)

    def test_view_post_by_tag_pagination_is_four(self):
        tag = Tag.objects.get(pk=1)
        url = reverse('blog:post_list_by_tag', kwargs={'slug': tag.slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertEqual(response.context['is_paginated'], True)
        self.assertTrue('page_obj' in response.context)
        self.assertTrue('paginator' in response.context)
        self.assertEqual(response.context['post_list'].count(), 4)

    def test_view_lists_all_posts_by_tag(self):
        # Get second page and confirm it has (exactly) remaining 1 items
        tag = Tag.objects.get(pk=1)
        url = reverse('blog:post_list_by_tag', kwargs={'slug': tag.slug})
        response = self.client.get(url, data={'page': 2})
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertEqual(response.context['is_paginated'], True)
        self.assertTrue('page_obj' in response.context)
        self.assertTrue('paginator' in response.context)
        self.assertEqual(response.context['post_list'].count(), 1)

    def test_view_get_queryset_published_and_tag_posts(self):
        tag = Tag.objects.get(pk=1)
        url = reverse('blog:post_list_by_tag', kwargs={'slug': tag.slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['post_list'].count(), 4)


class PostListByAuthorTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        n_posts = 5
        user = User.objects.create_superuser(username='admin', password='admin')
        Profile.objects.create(user=user, slug=slugify(user.username))
        title = 'FOO title'

        for index in range(n_posts):
            unique_title = title + str(index)
            post = Post.objects.create(title=unique_title,
                                       slug=slugify(unique_title),
                                       author=user,
                                       body='FOO body',
                                       status='published')
            post.tags.add('test')

    def test_view_url_exists_at_desired_location(self):
        url = '/blog/post/author/admin/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        profile = Profile.objects.get(pk=1)
        url = reverse('blog:post_list_by_author', kwargs={'slug': profile.slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_view_correct_template_used(self):
        template_name = 'blog/post/list_author.html'
        profile = Profile.objects.get(pk=1)
        url = reverse('blog:post_list_by_author', kwargs={'slug': profile.slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name)

    def test_view_context_object_names(self):
        profile = Profile.objects.get(pk=1)
        url = reverse('blog:post_list_by_author', kwargs={'slug': profile.slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue('post_list' in response.context)
        self.assertTrue('user' in response.context)

    def test_view_post_by_tag_pagination_is_four(self):
        profile = Profile.objects.get(pk=1)
        url = reverse('blog:post_list_by_author', kwargs={'slug': profile.slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertEqual(response.context['is_paginated'], True)
        self.assertTrue('page_obj' in response.context)
        self.assertTrue('paginator' in response.context)
        self.assertEqual(response.context['post_list'].count(), 4)

    def test_view_lists_all_posts_by_tag(self):
        # Get second page and confirm it has (exactly) remaining 1 items
        profile = Profile.objects.get(pk=1)
        url = reverse('blog:post_list_by_author', kwargs={'slug': profile.slug})
        response = self.client.get(url, data={'page': 2})
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertEqual(response.context['is_paginated'], True)
        self.assertTrue('page_obj' in response.context)
        self.assertTrue('paginator' in response.context)
        self.assertEqual(response.context['post_list'].count(), 1)

    def test_view_get_queryset_published_and_user_posts(self):
        profile = Profile.objects.get(pk=1)
        url = reverse('blog:post_list_by_author', kwargs={'slug': profile.slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['post_list'].count(), 4)


