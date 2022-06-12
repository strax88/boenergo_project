# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/
import os.path

from config.settings import BASE_DIR, PROJECT_ROOT

LANGUAGE_CODE = "ru"

TIME_ZONE = "Europe/Moscow"

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = [
    os.path.join(PROJECT_ROOT, "locale"),
]
