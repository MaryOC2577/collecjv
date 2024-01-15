import datetime
import pytest
from django.test import Client, TestCase
from login.models import PassChange


@pytest.mark.django_db
class TestLoginModel(TestCase):
    def test_passchange(self):
        passchange = PassChange.objects.create(
            email="test@test.fr",
            token="Dsojfpsosetijpjpzers",
            date=datetime.datetime.now(),
        )
        expected_value = "test@test.fr"
        assert str(passchange.email) == expected_value


class TestLoginViews(TestCase):
    def setUp(self):
        self.client = Client()

    def test_get(self):
        """views.get_context_data() sets 'name' in context."""
        # Setup request and view.
        response = self.client.get("/login/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "login.html")
