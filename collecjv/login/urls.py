from django.urls import path
from . import views
from login.views import registration, AccountView, PasswordReset
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("", views.LoginView.as_view(), name="login"),
    path("registration", registration, name="registration"),
    path("logout/", LogoutView.as_view(next_page="home"), name="logout"),
    path("account", views.AccountView.as_view(), name="account"),
    path("password_reset/<str:token>", views.NewPassword.as_view(), name="newpass"),
    path("pass_done", views.PasswordDone.as_view(), name="passdone"),
    path("forget_password/", PasswordReset.as_view(), name="passreset"),
]
