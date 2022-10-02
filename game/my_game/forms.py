from django.forms import ModelForm
from django import forms

from game.my_game.models import Game


class GameForm(ModelForm):
    class Meta:
        model = Game
        fields = "__all__"


class DeleteGameForm(GameForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs["disabled"] = "disabled"
            field.widget.attrs["readonly"] = "readonly"
