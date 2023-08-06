from django.urls import path

from .views import PronoteCatalogue


urlpatterns = [
    path("catalogue/<uai>", PronoteCatalogue.as_view(), name="pronote_catalogue"),
]
