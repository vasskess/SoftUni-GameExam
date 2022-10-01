from django.shortcuts import render


# Create your views here.


def create_game(request):
    return render(request, "my_game/create-game.html")


def game_details(request, id):
    return render(request, "my_game/details-game.html")


def edit_game(request, id):
    return render(request, "my_game/edit-game.html")


def delete_game(request, id):
    return render(request, "my_game/delete-game.html")
