import pytest
from django.test import TestCase
from collecjv.models import Company


@pytest.mark.django_db
class TestCompagny(TestCase):
    
    def test_compagny(self):
        compagny = Company.objects.create(
            name="test compagny",
            area="europe",
            developer=True,
            editor=True

        )

        expected_value = "test compagny"
        assert str(compagny.name) == expected_value
