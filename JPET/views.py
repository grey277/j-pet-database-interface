from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django import shortcuts
from .forms import *


# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render(request))


def runs(request):
    template = loader.get_template('runs.html')
    return HttpResponse(template.render(request))


def setups(request):
    template_base = 'setups.html'
    template_form = 'setupForm.html'

    if request.method == 'POST':
        #valid data and save
        form = SetupForm(request.POST)
    else:
        form = SetupForm()

    if request.is_ajax(): #if req is from ajax, send only form
        template_name = template_form
    else:
        template_name = template_base

    return shortcuts.render(request, template_name, {'form': form})


def faq(request):
    template = loader.get_template('faq.html')
    return HttpResponse(template.render(request))