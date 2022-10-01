from django.shortcuts import render


# Create your views here.


def create_game(request):
    return render(request, "create-game.html")


def game_details(request, id):
    return render(request, "details-game.html")


def edit_game(request, id):
    return render(request, "edit-game.html")


def delete_game(request, id):
    return render(request, "delete-game.html")
