from django.contrib import admin
from .models import AudioClip, AudioTag

admin.site.register(AudioTag)
admin.site.register(AudioClip)
