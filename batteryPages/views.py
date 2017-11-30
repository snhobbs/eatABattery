from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, Template
from django.core.mail import send_mail
from glob import glob
import os

def home(request):
    template = loader.get_template('pages/home.html')
    context = {}
    context.update({
        "description":"All things chargable and dischargable. A truly electric community.", 
        "title":"Hospital",
    })
    return HttpResponse(template.render(context, request))

def pj(request):
    template = loader.get_template('pages/grave.html')
    context = {}
    context.update({
        "description":"PJ The Party Pickle dancing on your grave suckka", 
        "title":"PJ The Party Pickle",
    })
    return HttpResponse(template.render(context, request))


def healthyLiving(request):
    template = loader.get_template('pages/healthyLiving.html')
    context = {}
    context.update({
        "description":"Battery health facts and calorie information", 
        "title":"Healthy Living",
    })
    return HttpResponse(template.render(context, request))

class Poem(object):
    def __init__(self, loc):
        self.loc = loc
        self.load()

    def load(self):
        self.title = self.loc.split('.')[0].replace('_', ' ').title().split('/')[-1]
        self.loadImg()

    def loadImg(self):
        imgTitle = "batteryPages/static/pages/{}.*".format(self.title.replace(' ', '_'))
        
        imgs = glob(imgTitle)
        if len(imgs) > 0:
            self.image = "/static/pages/" + glob(imgTitle)[0].split('/')[-1]
        else:
            self.image = ""

        self.poem = []
        with open(self.loc, 'r') as f:
            for line in f:
                self.poem.append(line + "<br>")
        self.poem = "".join(self.poem)

        self.makeCarouselObj()

    def makeCarouselObj(self):
        self.body = '''
            <h2 style='font-size:40px'>{}</h2>
            <div class='container' style='margin:40px;'></div>
            <p>{}</p>'''.format('{ ' + self.title + ' }', self.poem)
        self.number = 0

class Poems(object):
    def __init__(self, dirName):
        self.dirName = dirName
        self.poems = []
        for poem in glob(os.path.join(self.dirName, "*.txt")):
            self.poems.append(Poem(poem))

        self.makeCarouselContext()
    
    def makeCarouselContext(self):
        heroSlides = []
        for i, poem in enumerate(self.poems):
            poem.number = i 
            heroSlides.append(poem)
        self.context = ({
            "heroSlidesTop": heroSlides[0],
            "heroSlides": heroSlides[1:]
        })

def poems(request):
    
    template = loader.get_template('pages/poems.html')
    context = Poems("batteryPages/appData/poems").context
    context.update({
        "description":"Battery haikus", 
        "title":"Kirkland Corner",
    })
    return HttpResponse(template.render(context, request))

def bear(request):
    from .models import AudioClip
    
    template = loader.get_template('pages/bear.html')
    context = {
        "description":"Bear", 
        "title":"Bear",
        'mp3s':AudioClip.objects.filter(tagName__title = 'bear')
    }
    return HttpResponse(template.render(context, request))

def mgs(request):
    from .models import Video
    
    template = loader.get_template('pages/videoFeed.html')
    context = {
        "description":"Metal Gear Scholar", 
        "title":"Metal Gear Scholar",
        'videos':Video.objects.all()#filter(tagName__title = 'MGS')
    }
    return HttpResponse(template.render(context, request))
