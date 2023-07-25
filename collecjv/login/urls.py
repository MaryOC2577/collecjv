from django.urls import path
from . import views
from login.views import registration, logout
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("", views.LoginView.as_view(), name="login"),
    path("registration", registration, name="registration"),
    path('logout/', LogoutView.as_view(next_page="home"), name='logout'),
    #path("logout", logout, name="logout")
]
