import os

from django import views
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils.translation import gettext_lazy as _

from config.settings import STATIC_URL


class IndexView(TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        title = _("Index page")

        return render(
            request,
            self.template_name,
            {
                "title": title,
            },
        )


class DocsView(TemplateView):
    template_name = "README.html"

    def get(self, request, *args, **kwargs):
        title = _("Project documents")

        return render(
            request,
            self.template_name,
            {
                "title": title,
            },
        )
