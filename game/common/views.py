from django.shortcuts import render


# Create your views here.


def home(request):
    return render(request, "common/home-page.html")


def dashboard(request):
    return render(request, "common/dashboard.html")
