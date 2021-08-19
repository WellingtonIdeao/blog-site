from django.test import TestCase
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse
from ..models import Post


class PostListViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create 3 Post objects
        n_post = 3
        user = User.objects.create_superuser(username='admin', password='admin')
        for index in range(n_post):
            title = 'FOO text'
            unique_title = title+str(index)
            Post.objects.create(title=unique_title,
                                slug=slugify(unique_title),
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

    def test_view_list_all_posts(self):
        url = reverse('blog:post-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['post_list']), 0)



