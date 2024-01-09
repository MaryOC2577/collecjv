from django.shortcuts import render
from django.views.generic import View
from collecjv.models import Game


class SearchView(View):
    def get(self, request):
        return render(request, "search.html")
    

class GameSearchResult(View):
    template_name = "result.html"
    model = Game
    context_object_name = "games"

    def get_queryset(self):
        expression = self.request.GET.get("expression", "").title()
        print("expression :", expression)
        return Game.objects.filter(name__contains=expression).order_by("id") if expression else []

    def get_context_data(self, **kwargs):
        kwargs["expression"] = self.request.GET.get("expression", "")

        return super().get_context_data(**kwargs)
