from django.contrib import admin

from django.utils.translation import gettext_lazy as _

from modules.solving_quadratic_equations.models import QuadraticEquationSolving


@admin.register(QuadraticEquationSolving)
class QuadraticEquationSolvingAdmin(admin.ModelAdmin):
    _("""Admin panel for the QuadraticEquationSolving model""")

    list_display = [
        "a",
        "b",
        "c",
        "discriminant",
        "solution_1",
        "solution_2",
    ]
