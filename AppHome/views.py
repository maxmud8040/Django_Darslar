from django.shortcuts import render
from django.views.generic import TemplateView, ListView
# Create your views here.

class HomePageView(TemplateView):
    template_name = "News/index.html"