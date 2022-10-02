from django.db import models

# Create your models here.
from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.


class Profile(models.Model):
    email = models.EmailField()

    age = models.IntegerField(
        validators=[
            MinValueValidator(12),
        ],
    )

    password = models.CharField(
        max_length=30,
    )

    first_name = models.CharField(
        max_length=30,
        null=True,
        blank=True,
    )

    last_name = models.CharField(
        max_length=30,
        null=True,
        blank=True,
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )
