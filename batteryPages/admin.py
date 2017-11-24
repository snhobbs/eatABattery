from django.contrib import admin

from .models import Patent, PatentGroup, Case

admin.site.register(Patent)
admin.site.register(PatentGroup)
admin.site.register(Case)
