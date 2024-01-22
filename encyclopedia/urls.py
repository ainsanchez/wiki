from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:name>", views.title, name="title"),
    path("search/", views.search, name="search"),
    path("search_results", views.search, name="search_results")
]
