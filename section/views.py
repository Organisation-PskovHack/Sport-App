from django.shortcuts import render
from django.views.generic import TemplateView


class homePage(TemplateView):
    template_name = "page/home.html"
