from django.db import models
from django.utils.translation import gettext_lazy as _


class QuadraticEquationSolving(models.Model):
    _("""Model: Solution of the quadratic equation""")

    a = models.FloatField(verbose_name=_("Coefficient 'a'"), null=True)
    b = models.FloatField(verbose_name=_("Coefficient 'b'"), null=True)
    c = models.FloatField(verbose_name=_("Coefficient 'c'"), null=True)
    discriminant = models.FloatField(
        verbose_name=_("Discriminant"), null=True, default=None
    )
    solution_1 = models.FloatField(
        verbose_name=_("The first root of the equation `X1`"), null=True, default=None
    )
    solution_2 = models.FloatField(
        verbose_name=_("The first root of the equation `X2`"), null=True, default=None
    )

    def __str__(self):
        a = self.a
        if a == 1:
            str_a = "x^2"
        elif a == -1:
            str_a = "-x^2"
        elif a == 0:
            str_a = ""
        else:
            str_a = f"{a} * x^2"
        b = self.b
        if b == -1:
            str_b = f" - x"
        elif b == 1:
            str_b = f" + x"
        elif b == 0:
            str_b = f""
        elif b < 0:
            str_b = f" - {abs(b)} * x"
        else:
            str_b = f" + {b} * x"
        c = self.c
        if c == 0:
            str_c = f""
        elif c < 0:
            str_c = f" - {abs(c)}"
        else:
            str_c = f" + {c}"

        return (
            f"{str_a}{str_b}{str_c} = 0 "
            f"({_('Discriminant')}: {self.discriminant}; "
            f"X1: {self.solution_1}; "
            f"X2: {self.solution_2})"
        )

    class Meta:
        verbose_name = _("Solving the quadratic equation")
        verbose_name_plural = _("Solutions of quadratic equations")
        unique_together = (
            "a",
            "b",
            "c",
        )
        ordering = (
            "solution_1",
            "solution_2",
        )
