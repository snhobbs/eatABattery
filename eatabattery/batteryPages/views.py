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

class Poem(object):
    def __init__(self, loc):
        self.loc = loc
        
    def getTitle(self):
        self.title = ' '.join(loc.split('.')[0].split('_')).title()

    def getImage(self):
        self.image = "/static/duracell.jpg"

    def getBody(self):
        with open(self.loc, 'r') as f:
            self.poem = f.read()

def poems(request):
    from glob import glob
    poems = []
    for poem in glob("../appData/poems/*.txt"):
        poems.append(Poem(poem))
        print(poem)
    template = loader.get_template('pages/poems.html')
    
    context = {}
    context.update({
        "description":"Battery Love Poems", 
        "title":"Poems",
        "poems":poems
    })
    return HttpResponse(template.render(context, request))


