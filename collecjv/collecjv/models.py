""" Database models """

from django.db import models
from django.contrib.auth.models import AbstractUser


class Developper(models.Model):
    name = models.CharField(max_length=400, unique=True)


class Editor(models.Model):
    name = models.CharField(max_length=400, unique=True)
    area = models.CharField(max_length=400)


class Collection(models.Model):
    name = models.CharField(max_length=400, unique=True)
    description = models.CharField(max_length=400)


class Game(models.Model):
    name = models.CharField(max_length=400, unique=True)
    description = models.CharField(max_length=400)
    state = models.CharField(max_length=400)
    category = models.CharField(max_length=400)
    date = models.ManyToManyField(Editor, related_name='models', through='GameEditor')
    state = models.ManyToManyField(Collection, related_name='models', through='Collection')


class GameEditor(models.Model):
    editor = models.ForeignKey(Editor, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    date = models.DateField()


class GameCollection(models.Min):
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    state = models.CharField(max_length=400)


class GameUser(AbstractUser):
    username = models.TextField(unique=True)
    email = models.EmailField(("email address"), blank=True, unique=True)
