from django.test import TestCase
from .models import Post


class Modeltesting(TestCase):
    def setUp(self):
        self.blog = Post.objects.create(title="Xiaomi Flagship Phone", author="Nicholas Karimi", slug='xiaomi-device')

    def test_post_model(self):
        data = self.blog
        self.assertTrue(isinstance(data, Post))
        self.assertEqual(str(data), "Xiaomi Flagship Phone")
