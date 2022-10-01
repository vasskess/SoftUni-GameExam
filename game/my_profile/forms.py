from django.forms import ModelForm
from django import forms

from game.my_profile.models import Profile


class ProfileForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Profile
        fields = ("email", "age", "password")
