from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path("", RedirectView.as_view(url="/enquetes/")),  # redireciona a raiz
    path("enquetes/", include("enquetes.urls")),
    path("admin/", admin.site.urls),
]
