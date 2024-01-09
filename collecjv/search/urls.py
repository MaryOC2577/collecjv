from django.urls import path
from . import views


urlpatterns = [
    path("", views.SearchView.as_view(), name="search"),
    path("", views.GameSheet.as_view(), name="gamesheet"),
]
