from django.urls import path
from . import views

app_name = "enquetes"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:enquete_id>/", views.detail, name="detail"),
    path("<int:enquete_id>/vote/", views.vote, name="vote"),
    path("<int:enquete_id>/results/", views.results, name="results"),
]
