from django.urls import path
from game.my_game.views import *

urlpatterns = (
    path("create/", create_game, name="create-game"),
    path("details/<id>/", game_details, name="details-game"),
    path("edit/<id>/", edit_game, name="edit-game"),
    path("delete/<id>/", delete_game, name="delete-game"),
)
