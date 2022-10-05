# ...
from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.views import View  # <- View class to handle requests
# <- a class to handle sending a type of response
from django.http import HttpResponse


# Create your views here.
class Home(TemplateView):
    template_name = "home.html"


class About(TemplateView):
    template_name = "about.html"
