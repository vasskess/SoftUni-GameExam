from django.shortcuts import render

from game.my_profile import models


# Create your views here.


def home(request):
    profile = models.Profile.objects.first()
    context = {'profile': profile}
    return render(request, 'home-page.html', context=context)


def dashboard(request):
    return render(request, "dashboard.html")
