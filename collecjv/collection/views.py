from django.shortcuts import render
from django.views.generic import View


class CollectView(View):
    def get(self, request):
        return render(request, "collection.html")