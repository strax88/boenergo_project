# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
import os.path

from config.settings import PROJECT_ROOT, BASE_DIR

STATIC_URL = "static/"
STATIC_ROOT = os.path.join(PROJECT_ROOT, "static/")
#STATICFILES_DIRS = ["static/"]
