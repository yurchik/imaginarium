from django.contrib import admin

from .models import Picture


class PictureAdmin(admin.ModelAdmin):
    list_display = ['slug', 'views', 'rate', 'created', 'updated']
    exclude = ['views', 'rate']
    ordering = ['updated']

admin.site.register(Picture, PictureAdmin)
