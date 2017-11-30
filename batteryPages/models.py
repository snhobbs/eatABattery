from django.db import models
from mezzanine.core.fields import FileField
from django.utils.translation import ugettext_lazy as _
from mezzanine.utils.models import upload_to
from embed_video.fields import EmbedVideoField

class AudioTag(models.Model):
    title = models.CharField(max_length=75)
    def __str__(self):
        return self.title

class AudioClip(models.Model):
    title = models.CharField(max_length=75)
    description = models.TextField()
    mp3 = FileField(verbose_name=_("MP3"),
        upload_to=upload_to("AudioClip.mp3", "audio"),
        format='', max_length=255)
    tagName = models.ManyToManyField(AudioTag)

    def __str__(self):
        return self.title
    
class Video(models.Model):
    title = models.CharField(max_length=75, default="")
    description = models.TextField(default = "")
    video = EmbedVideoField()
    published = models.DateTimeField(auto_now=False, auto_now_add=False)
    def __str__(self):
        return self.title

