from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.

class Game(models.Model):
    title = models.CharField(
        max_length=15,
        unique=True,
    )

    category = models.CharField(
        max_length=15,
        choices=(
            ("Action", "Action"),
            ("Adventure", "Adventure"),
            ("Puzzle", "Puzzle"),
            ("Strategy", "Strategy"),
            ("Sports", "Sports"),
            ("Board/Card Game", "Board/Card Game"),
            ("Other", "Other"),
        )
    )

    rating = models.FloatField(
        validators=(
            MinValueValidator(0.1),
            MaxValueValidator(5.0),
        )
    )

    max_level = models.IntegerField(
        validators=(MinValueValidator(1),),                          #Maybe use MinValueValidator
        null=True,
        blank=True,
    )

    image_url = models.URLField(
    )

    summary = models.TextField(
        null=True,
        blank=True,
    )
