from django.test import TestCase
from django.contrib.auth.models import User
from blogging.models import Post
from blogging.models import Category


class PostTestCase(TestCase):
    fixtures = ['blogging_test_fixture.json', ]

    def setUp(self):
        self.user = User.objects.get(pk=1)

    def test_string_representation(self):
        expected = "This is a title"
        p1 = Post(title=expected)
        actual = str(p1)
        self.assertEqual(expected, actual)


class CategoryTestCase(TestCase):
    def test_string_representation(self):
        expected = "Category A"
        cat = Category(name=expected)
        actual = str(cat)
        self.assertEqual(expected, actual)
