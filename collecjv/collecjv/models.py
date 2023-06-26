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
    date = models.ManyToManyField(Editor, related_name='models', through='Editor')
    state = models.ManyToManyField(Collection, related_name='models', through='Collection')


class User(AbstractUser):
    username = models.TextField(unique=True)
    email = models.EmailField(_("email address"), blank=True, unique=True)
    password = models.TextField()



