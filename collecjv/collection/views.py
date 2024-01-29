from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import View, DetailView,ListView
from collecjv.models import Game, Collection


class CollectView(ListView):

    template_name ="collection.html"
    context_object_name = "collection"
    model = Collection

    def get_queryset(self) -> QuerySet[Any]:
        return super().get_queryset()
    

class OneGameView(DetailView):
    template_name = "game.html"

    context_object_name = "game"

    model = Game

    def get_context_data(self, **kwargs):
        self.request.session["game_id"] = self.get_object().id
        return super().get_context_data(**kwargs)
