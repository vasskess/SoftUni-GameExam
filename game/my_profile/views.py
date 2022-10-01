from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect

from game.my_profile.forms import ProfileForm


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
    return render(request, "my_profile/details-profile.html")


def edit_profile(request):
    return render(request, "my_profile/edit-profile.html")


def delete_profile(request):
    return render(request, "my_profile/delete-profile.html")