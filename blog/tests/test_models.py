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

    def test_publish_verbose_name(self):
        post = Post.objects.get(pk=1)
        field_name = post._meta.get_field('publish').verbose_name
        self.assertEqual(field_name, 'publish')

    def test_publish_is_blank_false(self):
        post = Post.objects.get(pk=1)
        is_blank = post._meta.get_field('publish').blank
        self.assertEqual(is_blank, False)

    def test_publish_is_null_false(self):
        post = Post.objects.get(pk=1)
        is_null = post._meta.get_field('publish').null
        self.assertEqual(is_null, False)

    def test_publish_auto_now_false(self):
        post = Post.objects.get(pk=1)
        is_auto_now = post._meta.get_field('publish').auto_now
        self.assertEqual(is_auto_now, False)

    def test_publish_auto_now_add_false(self):
        post = Post.objects.get(pk=1)
        is_auto_now_add = post._meta.get_field('publish').auto_now_add
        self.assertEqual(is_auto_now_add, False)

    def test_created_verbose_name(self):
        post = Post.objects.get(pk=1)
        field_name = post._meta.get_field('created').verbose_name
        self.assertEqual(field_name, 'created')

    def test_created_is_blank(self):
        post = Post.objects.get(pk=1)
        is_blank = post._meta.get_field('created').blank
        self.assertEqual(is_blank, True)

    def test_created_is_null_false(self):
        post = Post.objects.get(pk=1)
        is_null = post._meta.get_field('created').null
        self.assertEqual(is_null, False)

    def test_created_is_editable_false(self):
        post = Post.objects.get(pk=1)
        is_editable = post._meta.get_field('created').editable
        self.assertEqual(is_editable, False)

    def test_created_is_auto_now_add(self):
        post = Post.objects.get(pk=1)
        is_auto_now_add = post._meta.get_field('created').auto_now_add
        self.assertEqual(is_auto_now_add, True)

    def test_created_is_auto_now_false(self):
        post = Post.objects.get(pk=1)
        is_auto_now = post._meta.get_field('created').auto_now
        self.assertEqual(is_auto_now, False)

    def test_updated_verbose_name(self):
        post = Post.objects.get(pk=1)
        field_name = post._meta.get_field('updated').verbose_name
        self.assertEqual(field_name, 'updated')

    def test_updated_is_blank(self):
        post = Post.objects.get(pk=1)
        is_blank = post._meta.get_field('updated').blank
        self.assertEqual(is_blank, True)

    def test_updated_is_null_false(self):
        post = Post.objects.get(pk=1)
        is_null = post._meta.get_field('updated').null
        self.assertEqual(is_null, False)

    def test_updated_is_editable_false(self):
        post = Post.objects.get(pk=1)
        is_editable = post._meta.get_field('updated').editable
        self.assertEqual(is_editable, False)

    def test_updated_is_auto_now_add_false(self):
        post = Post.objects.get(pk=1)
        is_auto_now_add = post._meta.get_field('updated').auto_now_add
        self.assertEqual(is_auto_now_add, False)

    def test_updated_is_auto_now(self):
        post = Post.objects.get(pk=1)
        is_auto_now = post._meta.get_field('updated').auto_now
        self.assertEqual(is_auto_now, True)

    def test_status_verbose_name(self):
        post = Post.objects.get(pk=1)
        field_name = post._meta.get_field('status').verbose_name
        self.assertEqual(field_name, 'status')

    def test_status_max_length(self):
        post = Post.objects.get(pk=1)
        max_length = post._meta.get_field('status').max_length
        self.assertEqual(max_length, 10)

    def test_status_default_value(self):
        post = Post.objects.get(pk=1)
        default = post._meta.get_field('status').default
        self.assertEqual(default, 'draft')

    def test_post_ordering(self):
        post = Post.objects.get(pk=1)
        ordering = post._meta.ordering
        self.assertEqual(ordering[0], '-publish')

    def test_post_verbose_name_plural(self):
        post = Post.objects.get(pk=1)
        verbose_name_plural = post._meta.verbose_name_plural
        self.assertEqual(verbose_name_plural, 'posts')

    def test_post_verbose_name(self):
        post = Post.objects.get(pk=1)
        verbose_name = post._meta.verbose_name
        self.assertEqual(verbose_name, 'post')

    def test_object_name_is_title(self):
        post = Post.objects.get(pk=1)
        expected_name = post.title
        self.assertEqual(str(post), expected_name)

    def test_status_choices_length(self):
        post = Post.objects.get(pk=1)
        choices = post._meta.get_field('status').choices
        self.assertEqual(len(choices), 2)

    def test_get_absolute_url(self):
        post = Post.objects.get(pk=1)
        url = post.get_absolute_url()
        expected_url = f'/blog/post/{post.slug}/'
        self.assertEqual(url, expected_url)










