from django.shortcuts import render, redirect

from game.my_game.forms import GameForm, DeleteGameForm
from game.my_game.models import Game


# Create your views here.


def create_game(request):
    form = GameForm

    if request.method == "POST":
        form = GameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("dashboard")
    context = {"form": form}
    return render(request, "my_game/create-game.html", context)


def game_details(request, id):
    game = Game.objects.get(id=id)
    context = {"game": game}

    return render(request, "my_game/details-game.html", context)


def edit_game(request, id):
    game = Game.objects.get(id=id)
    form = GameForm(instance=game)

    if request.method == "POST":
        form = GameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect("dashboard")

    context = {"game": game, "form": form}
    return render(request, "my_game/edit-game.html", context)


def delete_game(request, id):
    game = Game.objects.get(id=id)
    form = DeleteGameForm(instance=game)

    if request.method == "POST":
        game.delete()
        return redirect("dashboard")
    context = {"game": game, "form": form}
    return render(request, "my_game/delete-game.html", context)
