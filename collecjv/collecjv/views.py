from django.views.generic import View
from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.contrib.auth import authenticate, login
from django.contrib import messages
from models import GameUser
from django.http.response import HttpResponse


class Home(TemplateView):
    template_name = "base.html"


class LoginView(View):
    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        """Authenticate a user."""

        # Step 1 :
        email = username = request.POST["username"]
        password = request.POST["password"]

        # Step 2 :
        user = authenticate(request, email=email, username=username, password=password)

        # Step 3 :
        if user is not None:
            login(request, user)
            messages.add_message(request, messages.SUCCESS, "Vous êtes connecté !")
            return redirect("account")
        else:
            messages.add_message(
                request, messages.ERROR, "Les champs renseignés sont invalides."
            )
            return render(request, "login.html")
        

def registration(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        if password1 != password2:
            return render(
                request,
                "registration.html",
                {"error": "Les mots de passe de correspondent pas."},
            )

        GameUser.objects.create_user(username=username, email=email, password=password1)
        return HttpResponse(f"Bienvenue {username} !")

    return render(request, "registration.html")