from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:name>", views.title, name="title"),
    path("search/", views.search, name="search"),
    path("search_results", views.search, name="search_results"),
    path("create_entry", views.create, name="create_entry"),
    path("edit/<str:title>", views.edit, name="edit"),
    path("random", views.random, name="random")
]
