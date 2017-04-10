from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.template import loader
from bakery.views import BuildableTemplateView
import csv

# Create your views here.

class MainView(BuildableTemplateView):
    template_name = 'interactivechart/index.html'
    build_path = 'admission-trends/index.html'