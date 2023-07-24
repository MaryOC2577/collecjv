from django.urls import path
from . import views
from login.views import registration

urlpatterns = [
    path("", views.LoginView.as_view(), name="login"),
    path("registration", registration, name="registration")
]
