from django.urls import path
from . import views


urlpatterns = [
    path("", views.SearchView.as_view(), name="search"),
    path("result", views.GameSearchResult.as_view(), name="result"),
]
