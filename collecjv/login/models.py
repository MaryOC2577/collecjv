from django.db import models


class PassChange(models.Model):
    email = models.EmailField("email address")
    token = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
