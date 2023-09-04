from django.urls import path
from . import views


urlpatterns = [
    path("", views.CollectView.as_view(), name="collection"),
    path("onegame/<int:pk>/", views.OneGameView.as_view(), name="onegame"),
]
