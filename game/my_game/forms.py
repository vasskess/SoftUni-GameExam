from django.forms import ModelForm
from django import forms

from game.my_game.models import Game


class GameForm(ModelForm):
    class Meta:
        model = Game
        fields = "__all__"
