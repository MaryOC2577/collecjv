import pytest
from django.test import TestCase
from collecjv.models import Company


@pytest.mark.django_db
# @pytest.mark.transactional_db
# @pytest.mark.django_db(transaction=True)
class TestCompagny(TestCase):
    compagny = Company.objects.create(
        name="test compagny",
        area="europe",
        developer=True,
        editor=True

    )
    expected_value = "test compagny"
    assert str(compagny.name) == expected_value
