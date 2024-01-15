from django.shortcuts import render
from django.views.generic import View, DetailView
from collecjv.models import Game


class SearchView(View):
    def get(self, request):
        return render(request, "search.html")


class GameSearchResult(DetailView):
    template_name = "result.html"
    model = Game
    context_object_name = "games"

    def get_object(self):
        expression = self.request.GET.get("expression", "").title()
        return (
            Game.objects.filter(name__contains=expression).order_by("id")
            if expression
            else []
        )

    def get_context_data(self, **kwargs):
        kwargs["expression"] = self.request.GET.get("expression", "")

        return super().get_context_data(**kwargs)
