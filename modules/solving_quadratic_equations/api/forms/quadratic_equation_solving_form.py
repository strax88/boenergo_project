from django import forms
from django.utils.translation import gettext_lazy as _

from modules.solving_quadratic_equations.services import QuadraticEquationSolvingService


class QuadraticEquationSolvingForm(forms.Form):
    _("""Form: Solving the quadratic equation""")
    a = forms.FloatField(
        label="",
        required=False,
        widget=forms.NumberInput(attrs={"placeholder": _("Coefficient 'a'")}),
    )
    b = forms.FloatField(
        label="",
        required=False,
        widget=forms.NumberInput(attrs={"placeholder": _("Coefficient 'b'")}),
    )
    c = forms.FloatField(
        label="",
        required=False,
        widget=forms.NumberInput(attrs={"placeholder": _("Coefficient 'c'")}),
    )

    def is_valid(self):
        _("""Basic and additional validations""")
        super().is_valid()
        QuadraticEquationSolvingService.validate_coefficient(self.cleaned_data)
