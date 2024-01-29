""" Database models """

from django.db import models
from django.contrib.auth.models import AbstractUser


class Company(models.Model):
    name = models.CharField(max_length=400, unique=True)
    area = models.CharField(max_length=400)
    developer = models.BooleanField(default=False, null=True)
    editor = models.BooleanField(default=False, null=True)


class Collection(models.Model):
    name = models.CharField(max_length=400, unique=True)
    description = models.CharField(max_length=400, blank=True, null=True)


class Platform(models.Model):
    name = models.CharField(max_length=400, unique=True)
    description = models.CharField(max_length=400, blank=True, null=True)


class Game(models.Model):
    name = models.CharField(max_length=400, unique=True)
    description = models.CharField(max_length=400, blank=True, null=True)
    category = models.CharField(max_length=400, blank=True, null=True)
    platform = models.ForeignKey(
        Platform, on_delete=models.DO_NOTHING, blank=True, null=True
    )
    company = models.ManyToManyField(
        Company, related_name="models", through="GameCompany", blank=True, null=True
    )
    state = models.ManyToManyField(
        Collection,
        related_name="models",
        through="GameCollection",
        blank=True,
        null=True,
    )


class GameCompany(models.Model):
    # ajouter blank
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, blank=True)
    date = models.DateField(blank=True, null=True)


class GameCollection(models.Model):
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    state = models.CharField(max_length=400)


class GameUser(AbstractUser):
    username = models.TextField(unique=True)
    email = models.EmailField(("email address"), blank=True, unique=True)
