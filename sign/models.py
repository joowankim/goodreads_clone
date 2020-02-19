from django.db import models

class User(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(
        verbose_name='email',
        max_length=255,
        unique=True
    )
    password = models.CharField(max_length=30)