from django.test import TestCase
from django.utils.text import slugify
from django.contrib.auth.models import User
from ..models import Post


class PostModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_superuser(username='admin', password='admin')
        title = 'FOO text'
        Post.objects.create(title=title,
                            slug=slugify(title),
                            author=user,
                            body='FOO body')

    def test_title_verbose_name(self):
        post = Post.objects.get(pk=1)
        field_name = post._meta.get_field('title').verbose_name
        self.assertEqual(field_name, 'title')

    def test_title_max_length(self):
        post = Post.objects.get(pk=1)
        max_length = post._meta.get_field('title').max_length
        self.assertEqual(max_length, 250)

    def test_title_is_unique(self):
        post = Post.objects.get(pk=1)
        is_unique = post._meta.get_field('title').unique
        self.assertEqual(is_unique, True)

    def test_title_is_blank_false(self):
        post = Post.objects.get(pk=1)
        is_blank = post._meta.get_field('title').blank
        self.assertEqual(is_blank, False)

    def test_title_is_null_false(self):
        post = Post.objects.get(pk=1)
        is_null = post._meta.get_field('title').null
        self.assertEqual(is_null, False)

    def test_slug_verbose_name(self):
        post = Post.objects.get(pk=1)
        field_name = post._meta.get_field('slug').verbose_name
        self.assertEqual(field_name, 'slug')

    def test_slug_max_length(self):
        post = Post.objects.get(pk=1)
        max_length = post._meta.get_field('slug').max_length
        self.assertEqual(max_length, 250)

    def test_slug_is_unique(self):
        post = Post.objects.get(pk=1)
        is_unique = post._meta.get_field('slug').unique
        self.assertEqual(is_unique, True)

    def test_slug_is_blank_false(self):
        post = Post.objects.get(pk=1)
        is_blank = post._meta.get_field('slug').blank
        self.assertEqual(is_blank, False)

    def test_slug_is_null_false(self):
        post = Post.objects.get(pk=1)
        is_null = post._meta.get_field('slug').null
        self.assertEqual(is_null, False)

    def test_author_verbose_name(self):
        post = Post.objects.get(pk=1)
        field_name = post._meta.get_field('author').verbose_name
        self.assertEqual(field_name, 'author')

    def test_body_verbose_name(self):
        post = Post.objects.get(pk=1)
        field_name = post._meta.get_field('body').verbose_name
        self.assertEqual(field_name, 'body')

    def test_body_is_blank_false(self):
        post = Post.objects.get(pk=1)
        is_blank = post._meta.get_field('body').blank
        self.assertEqual(is_blank, False)

    def test_body_is_null_false(self):
        post = Post.objects.get(pk=1)
        is_null = post._meta.get_field('body').null
        self.assertEqual(is_null, False)





