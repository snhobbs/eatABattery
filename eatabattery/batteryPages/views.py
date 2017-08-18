from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, Template
from django.core.mail import send_mail


def home(request):
    template = loader.get_template('pages/home.html')
    context = {}
    context.update({
        "description":"Hobbs ElectroOptics Home Page", 
        "title":"Home",
    })
    return HttpResponse(template.render(context, request))

def pj(request):
    template = loader.get_template('pages/grave.html')
    context = {}
    context.update({
        "description":"Hobbs ElectroOptics Home Page", 
        "title":"Home",
    })
    return HttpResponse(template.render(context, request))


def healthyLiving(request):
    template = loader.get_template('pages/healthyLiving.html')
    context = {}
    context.update({
        "description":"Hobbs ElectroOptics Home Page", 
        "title":"Home",
    })
    return HttpResponse(template.render(context, request))


