# ...
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.shortcuts import render
from django.views import View  # <- View class to handle requests
# <- a class to handle sending a type of response
from django.http import HttpResponse
from .models import Pepper


# Create your views here.
class Home(TemplateView):
    template_name = "home.html"


class About(TemplateView):
    template_name = "about.html"


class PepperList(TemplateView):
    template_name = "pepper_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["peppers"] = Pepper.objects.filter(
                common_name__icontains=name)
            context["header"] = f"Searching for {name}"
        else:
            context["peppers"] = Pepper.objects.all()
            context["header"] = "Trending Peppers"
        return context


class PepperCreate(CreateView):
    model = Pepper
    fields = ['common_name', 'name', 'origin', 'scoville', 'img']
    template_name = "pepper_create.html"
    success_url = "/peppers/"


class PepperDetail(DetailView):
    model = Pepper
    template_name = "pepper_detail.html"


class PepperUpdate(UpdateView):
    model = Pepper
    fields = ['common_name', 'name', 'origin', 'scoville', 'img']
    template_name = "pepper_update.html"
    success_url = "/peppers/"


class PepperDelete(DeleteView):
    model = Pepper
    template_name = "pepper_delete_confirmation.html"
    success_url = "/peppers/"
