from rest_framework.routers import DefaultRouter

from .api import QuadraticEquationSolvingAPI, QuadraticEquationSolvingView
from django.urls import path, include

router = DefaultRouter()

urlpatterns = [
    path(
        "", QuadraticEquationSolvingView.as_view(), name="solving_quadratic_equations"
    ),
    path("", include(router.urls)),
    path(
        r"api/",
        QuadraticEquationSolvingAPI.as_view({"get": "get", "post": "post"}),
    ),
]
