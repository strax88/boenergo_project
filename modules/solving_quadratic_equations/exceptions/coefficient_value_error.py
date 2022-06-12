from rest_framework.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class CoefficientValueError(ValidationError):
    _("""General class of exceptions by coefficient value""")

    message: str = _(
        "Base coefficient value error {coefficient_name}: {coefficient_value}"
    )

    def __init__(self, coefficient_name, coefficient_value):
        self.coefficient_name = coefficient_name
        self.coefficient_value = coefficient_value
        self.message = self.message.format(
            coefficient_name=self.coefficient_name,
            coefficient_value=self.coefficient_value,
        )
        super().__init__(self.message)


class CoefficientEmptyValueError(CoefficientValueError):
    _("""Class of exceptions based on an empty coefficient value""")

    message: str = _("Empty value `{coefficient_name}`: {coefficient_value}")


class CoefficientZeroValueError(CoefficientValueError):
    _("""Class of exceptions based on the zero value of the coefficient""")

    message: str = _("Zero value `{coefficient_name}`: {coefficient_value}")


class CoefficientWrongValueError(CoefficientValueError):
    _("""Class of exceptions for incorrect coefficient value""")

    message: str = _("Wrong value `{coefficient_name}`: {coefficient_value}")


class CoefficientInfinityValueError(CoefficientValueError):
    _("""Class of exceptions by infinite coefficient value""")

    message: str = _("Infinity value `{coefficient_name}`: {coefficient_value}")
