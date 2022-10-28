from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models




class Game(models.Model):
    RATING_MIN_VALUE = 0.1
    RATING_MAX_VALUE = 5.0

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
        ),
    )

    rating = models.FloatField(
        validators=(
            MinValueValidator(RATING_MIN_VALUE, message=f'The rating can be between {RATING_MIN_VALUE} and {RATING_MAX_VALUE}'),
            MaxValueValidator(RATING_MAX_VALUE, message=f'The rating can be between {RATING_MIN_VALUE} and {RATING_MAX_VALUE}'),
        )
    )

    max_level = models.IntegerField(
        validators=(MinValueValidator(1, message="The max level cannot be below 1"),),  # Maybe use MinValueValidator
        null=True,
        blank=True,
    )

    image_url = models.URLField(verbose_name="Image URL")

    summary = models.TextField(
        null=True,
        blank=True,
    )
