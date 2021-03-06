from django.http import HttpResponse
from django.template import loader
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django.shortcuts import redirect
from animals.models import Animal


class HomePageView(TemplateView):
    template_name = "homepage.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["animal_data"] = Animal.objects.all()
        context["title"] = "Главная страница"
        return context


class AnimalsPageView(ListView):
    template_name = "animals.html"
    model = Animal
    paginate_by = 6
    context_object_name = "animal_data"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "- Список животных"
        return context



class AnimalPageView(DetailView):
    template_name = "animal.html"
    model = Animal
    context_object_name = "animal_data"


class ContactsView(TemplateView):
    template_name = "contacts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Контакты"
        return context
