from rest_framework import serializers
from django.utils.translation import gettext_lazy as _

from modules.solving_quadratic_equations.services import (
    QuadraticEquationSolvingService,
)


class QuadraticEquationSolvingSerializer(serializers.Serializer):
    _("""Serializer: Solving the quadratic equation""")

    a = serializers.FloatField(required=False)
    b = serializers.FloatField(required=False)
    c = serializers.FloatField(required=False)

    def is_valid(self, raise_exception=False):
        _("""Basic and additional validations""")
        super().is_valid(raise_exception)
        QuadraticEquationSolvingService.validate_coefficient(self.validated_data)
