from django.contrib import admin
from .models import AudioClip, AudioTag, Video
from embed_video.admin import AdminVideoMixin, AdminVideoWidget

class VideoAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(Video)#, VideoAdmin)
#admin.site.register(VideoAdmin)

admin.site.register(AudioTag)
admin.site.register(AudioClip)
