from django.test import TestCase


class TestFirst(TestCase):

    def test_first(self):
        a = "test"
        self.assertEqual(a, "test")
