from typing import Optional, Union, Tuple, Dict, Any

from django.utils.translation import gettext_lazy as _

from modules.solving_quadratic_equations.enums import Coefficient
from modules.solving_quadratic_equations.exceptions import (
    CoefficientValueError,
    CoefficientInfinityValueError,
    CoefficientWrongValueError,
    CoefficientEmptyValueError,
)
from modules.solving_quadratic_equations.models import QuadraticEquationSolving


class QuadraticEquationSolvingService:
    _("""Service: Solving the quadratic equation""")

    @classmethod
    def calc_equation(
        cls, raw_coefficients: Dict
    ) -> Tuple[float, Union[Tuple, float, None]]:
        _("""Solution of the equation""")
        cls.validate_coefficient(raw_coefficients)
        cleaned_coefficients = cls.float_formatting_coefficient(**raw_coefficients)
        solving = cls.get_or_create_solving(cleaned_coefficients)
        result = None
        # если решение хранится в базе
        if solving.solution_1:
            result = solving.solution_1
        if solving.solution_2:
            result = (solving.solution_1, solving.solution_2)
        # если решения нет в базе - расчёт линейного уравнения
        if not solving.a and not result:
            solving.solution_1 = cls._calc_linear_equation(solving)
            solving.discriminant = None
            solving.save()
            result = solving.solution_1
        # если решения нет в базе - расчёт квадратного уравнения
        elif not solving.discriminant and not result:
            solving.discriminant = cls._find_discriminant(solving)
            solving.save()
            result = cls._find_solutions(solving)

        return solving.discriminant, result

    @classmethod
    def float_formatting_coefficient(cls, a: str, b: str, c: str) -> Coefficient:
        _("""Converting coefficients to real numbers and packing into namedtuple""")
        return Coefficient(*map(float, (a, b, c)))

    @classmethod
    def get_or_create_solving(
        cls, cleaned_coefficient: Coefficient
    ) -> QuadraticEquationSolving:
        _("""Fetching data from the database or adding data to the database""")
        solving = QuadraticEquationSolving.objects.filter(
            a=cleaned_coefficient.a,
            b=cleaned_coefficient.b,
            c=cleaned_coefficient.c,
        ).first()
        if not solving:
            solving = QuadraticEquationSolving.objects.create(
                **cleaned_coefficient._asdict()
            )

        return solving

    @classmethod
    def validate_coefficient(cls, raw_coefficients: Dict) -> None:
        _(
            """Data validation
        - coefficients `a` and `b` are present and not equal to zero;
        - coefficients are not equal to infinity;
        - coefficients are real numbers;
        """
        )
        if not raw_coefficients["a"] and not raw_coefficients["b"]:
            raise CoefficientValueError(
                ("a", "b"), (raw_coefficients["a"], raw_coefficients["b"])
            )
        for coefficient_name, coefficient_value in raw_coefficients.items():
            if coefficient_value and "inf" in str(coefficient_value):
                raise CoefficientInfinityValueError(coefficient_name, coefficient_value)
            if coefficient_value and not cls._checking_real_number(coefficient_value):
                raise CoefficientWrongValueError(coefficient_name, coefficient_value)
            if not coefficient_value:
                raise CoefficientEmptyValueError(coefficient_name, coefficient_value)

    @classmethod
    def _calc_linear_equation(cls, solution: QuadraticEquationSolving) -> float:
        _("""Solving a linear equation""")
        return -(solution.c / solution.b)

    @classmethod
    def _checking_real_number(cls, value: Any) -> bool:
        _(
            """Checking the value for belonging to real numbers
        (except for infinities)"""
        )
        return all([item.isdigit() for item in str(value).lstrip("-").split(".")])

    @classmethod
    def _find_discriminant(cls, solution: QuadraticEquationSolving) -> float:
        _("""Finding the discriminant""")
        return (solution.b**2) - 4 * solution.a * solution.c

    @classmethod
    def _find_first_solution(
        cls, solution: QuadraticEquationSolving, discriminant: float = 0
    ) -> float:
        _("""Finding the first root of the equation""")
        return (-solution.b + discriminant) / (2 * solution.a)

    @classmethod
    def _find_second_solution(
        cls, solution: QuadraticEquationSolving, discriminant: float
    ) -> float:
        _("""Finding the second root of the equation""")
        return (-solution.b - discriminant) / (2 * solution.a)

    @classmethod
    def _find_solutions(
        cls, solution: QuadraticEquationSolving
    ) -> Optional[Union[float, Tuple]]:
        _("""Finding the solutions of the equation""")
        if solution.discriminant < 0:
            return None
        elif solution.discriminant == 0.0:
            solution.solution_1 = cls._find_first_solution(solution)
            solution.save()
            return solution.solution_1
        sqrt_discriminant = solution.discriminant ** (1 / 2)
        solution.solution_1 = cls._find_first_solution(solution, sqrt_discriminant)
        solution.solution_2 = cls._find_second_solution(solution, sqrt_discriminant)
        solution.save()
        return (
            solution.solution_1,
            solution.solution_2,
        )
