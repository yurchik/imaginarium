from django.conf.urls import url
from imageLoad.views import IndexView, ImageView, ajax_like
from django.views.generic import ListView

from .models import Picture

app_name = 'imageLoad'

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^popular/$', ListView.as_view(template_name='imageLoad/popularListView.html',
                                        queryset=Picture.objects.order_by('-views').all()[:12]
                                        ), name='popular'),
    url(r'^top/$', ListView.as_view(template_name='imageLoad/popularListView.html',
                                        queryset=Picture.objects.order_by('-rate').all()[:12]
                                        ), name='top'),
    url(r'increase_and_get_like/', ajax_like, name='ajaxLike'),
    url(r'^(?P<slug>[^\.]+)$', ImageView.as_view(), name='detail_img'),
]
