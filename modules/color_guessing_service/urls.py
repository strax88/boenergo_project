from django.urls import path, include

from modules.color_guessing_service import views

urlpatterns = [
    path("", views.index),
]
