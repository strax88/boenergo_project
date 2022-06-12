from collections import OrderedDict
from typing import Union, Dict

from django.utils.translation import gettext_lazy as _
from django import views
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response

from modules.solving_quadratic_equations.api.forms import (
    QuadraticEquationSolvingForm,
)
from modules.solving_quadratic_equations.api.serializers import (
    QuadraticEquationSolvingSerializer,
)
from modules.solving_quadratic_equations.enums import Coefficient
from modules.solving_quadratic_equations.exceptions import CoefficientValueError
from modules.solving_quadratic_equations.models import QuadraticEquationSolving

from modules.solving_quadratic_equations.services import (
    QuadraticEquationSolvingService,
)


class QuadraticEquationSolvingView(views.generic.TemplateView):
    template_name = "find_solutions.html"
    form_class = QuadraticEquationSolvingForm
    initial: QuadraticEquationSolving = QuadraticEquationSolving.objects.none()
    service = QuadraticEquationSolvingService

    def _get_linear_badge(self) -> bool:
        _("""Get a feature `linear`""")
        return self.initial.discriminant is None and self.initial.solution_1 is not None

    def _get_non_solution_badge(self) -> bool:
        _("""Get a feature `non_solution`""")
        return self.initial.discriminant and self.initial.discriminant < 0

    def _get_one_solution_badge(self) -> bool:
        _("""Get a feature `one_solution`""")
        return (
            self.initial.solution_1 is not None
            and self.initial.solution_2 is None
            and not self._get_linear_badge()
        )

    def _get_two_solutions_badge(self) -> bool:
        _("""Get a feature `two_solutions`""")
        return (
            self.initial.solution_1 is not None and self.initial.solution_2 is not None
        )

    def _fill_data(self, request) -> Dict:
        _("""Fill data for rendered template""")
        form_data = {
            "a": None,
            "b": None,
            "c": None,
        }
        data = {
            "header": _("Solving the quadratic equation"),
            "form": None,
            "linear": None,
            "discriminant": None,
            "non_solution": None,
            "one_solution": None,
            "two_solutions": None,
            "solution_1": None,
            "solution_2": None,
            "error_message": None,
        }
        if request.POST:
            try:
                data["form"] = self.form_class(request.POST)
                data["form"].is_valid()
                self.service.calc_equation(data["form"].cleaned_data)
                cleaned_coefficient = Coefficient(*data["form"].cleaned_data.values())
                self.initial = self.service.get_or_create_solving(cleaned_coefficient)
            except CoefficientValueError as e:
                data["error_message"] = e.message

        if self.initial:
            # form_data["a"] = self.initial.a
            # form_data["b"] = self.initial.b
            # form_data["c"] = self.initial.c
            data["discriminant"] = self.initial.discriminant
            data["solution_1"] = self.initial.solution_1
            data["solution_2"] = self.initial.solution_2
            data["linear"] = self._get_linear_badge()
            data["non_solution"] = self._get_non_solution_badge()
            data["one_solution"] = self._get_one_solution_badge()
            data["two_solutions"] = self._get_two_solutions_badge()

        data["form"] = self.form_class(data=form_data)

        return data

    def get(self, request, *args, **kwargs):
        _("""GET-method handler""")
        request.GET = {}
        data = self._fill_data(request)
        return render(
            request,
            self.template_name,
            data,
        )

    def post(self, request, *args, **kwargs):
        _("""POST-method handler""")
        data = self._fill_data(request)
        return render(
            request,
            self.template_name,
            data,
        )


class QuadraticEquationSolvingAPI(viewsets.ViewSet):
    _("""API: Solving the quadratic equation""")

    serializer_class = QuadraticEquationSolvingSerializer
    service_class = QuadraticEquationSolvingService

    def get_raw_coefficients_from_request(
        self, request: Union[WSGIRequest, Request]
    ) -> Dict:
        _("""Get raw coefficient data from request""")
        request_data = {}
        if request.GET:
            request_data = request.GET.copy()
        elif request and hasattr(request, "data"):
            request_data = request.data.copy()
        elif request.POST and hasattr(request, "body"):
            request_data = request.body
        raw_coefficients = {
            "a": request_data.get("a", 0),
            "b": request_data.get("b", 0),
            "c": request_data.get("c", 0),
        }

        serializer = self.serializer_class(data=raw_coefficients)
        serializer.is_valid(raise_exception=True)
        return serializer.data

    @action(methods=["get"], detail=False)
    def get(self, request):
        _("""GET-method handler""")
        raw_coefficients = self.get_raw_coefficients_from_request(request)
        data = OrderedDict()
        data.update(raw_coefficients)
        discriminant, result = self.service_class.calc_equation(raw_coefficients)
        data["discriminant"] = discriminant
        data["result"] = result
        return Response(data)
