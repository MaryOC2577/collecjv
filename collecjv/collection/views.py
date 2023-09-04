from django.shortcuts import render
from django.views.generic import View, DetailView
from collecjv.models import Game


class CollectView(View):
    def get(self, request):
        return render(request, "collection.html")
    

class OneGameView(DetailView):
    
    template_name = "game.html"

    context_object_name = "game"

    model = Game

    def get_context_data(self, **kwargs):
        self.request.session["game_id"] = self.get_object().id
        return super().get_context_data(**kwargs)