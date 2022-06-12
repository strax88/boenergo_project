from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class SolvingQuadraticEquationsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "modules.solving_quadratic_equations"
    verbose_name = _("Module for finding solutions to quadratic equations")
