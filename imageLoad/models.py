from django.db import models
from django.conf import settings

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

from .utils import create_shortcode

SHORTCODE_MAX = getattr(settings, "SHORTCODES_MAX", 15)


# Create your models here.
class Picture(models.Model):
    img = models.ImageField(upload_to='uploads/')
    img_thumbnail = ImageSpecField(source='img',
                                   processors=[ResizeToFill(100, 100)],
                                   format='JPEG',
                                   options={'quality': 60})
    desc = models.CharField(max_length=200, default='Описание картинки не задано')
    slug = models.SlugField(max_length=200, unique=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    views = models.IntegerField(default=0)
    rate = models.IntegerField(default=0)

    def __str__(self):
        return self.slug

    def get_absolute_url(self):
        return '/{}'.format(self.slug)

    def save(self, *args, **kwargs):
        if not self.slug or self.slug == "":
            self.slug = create_shortcode(self)
        super(Picture, self).save(*args, **kwargs)

