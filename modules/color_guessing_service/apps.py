from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ColorGuessingServiceConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "modules.color_guessing_service"
    verbose_name = _("Module for color guessing")
