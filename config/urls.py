"""boenergo_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from modules import IndexView, DocsView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", IndexView.as_view(), name="index"),
    path("docs/", DocsView.as_view(), name="docs"),
    path("color_guessing_service/", include("modules.color_guessing_service.urls")),
    path(
        "solving_quadratic_equations/",
        include("modules.solving_quadratic_equations.urls"),
    ),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
