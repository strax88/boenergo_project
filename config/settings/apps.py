DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
]

CUSTOM_APPS = ["modules.color_guessing_service", "modules.solving_quadratic_equations"]

INSTALLED_APPS = DJANGO_APPS + CUSTOM_APPS
