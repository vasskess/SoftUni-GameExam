from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect

from game.my_game.models import Game
from game.my_profile.forms import ProfileForm, EditProfileForm
from game.my_profile.models import Profile


# Create your views here.


def create_profile(request):
    form = ProfileForm

    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home-page")
    context = {"form": form}
    return render(request, "my_profile/create-profile.html", context)


def profile_details(request):
    profile = Profile.objects.first()
    total_games = Game.objects.all()

    total_rating = sum([game.rating for game in total_games])

    try:
        average = total_rating / len(total_games)
    except ZeroDivisionError:
        average = 0.0

    context = {"profile": profile, "total_games": total_games, "average": average}
    return render(request, "my_profile/details-profile.html", context)


def edit_profile(request):
    profile = Profile.objects.first()
    form = EditProfileForm(instance=profile)

    if request.method == "POST":
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("details-profile")

    context = {"profile": profile, "form": form}
    return render(request, "my_profile/edit-profile.html", context)


def delete_profile(request):
    profile = Profile.objects.first()
    games = Game.objects.all()

    if request.method == "POST":
        profile.delete()
        games.delete()
        return redirect("home-page")

    return render(request, "my_profile/delete-profile.html")
