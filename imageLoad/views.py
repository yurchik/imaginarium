from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from django.shortcuts import redirect
from django.contrib import messages
from django.db.models import F

from django.http.response import JsonResponse

from .forms import ImageForm
from .models import Picture


# Create your views here.
class IndexView(TemplateView):
    template_name = 'imageLoad/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        form = ImageForm()
        context['latest_pictures'] = Picture.objects.order_by('-created')[0:12]
        context['form'] = form
        return context

    def post(self, request,  *args, **kwargs):
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            new_picture = form.save()
            messages.add_message(request, messages.SUCCESS, 'Ваша картинка успішно додана!')
            return redirect(new_picture.get_absolute_url())
        else:
            print(form.errors)
            return redirect('/')


class ImageView(DetailView):
    template_name = 'imageLoad/detail.html'
    model = Picture
    pk_url_kwarg = None

    def get_context_data(self, **kwargs):
        context = super(ImageView, self).get_context_data(**kwargs)
        picture = context['object']
        picture.views = F('views') + 1
        picture.save()
        picture.refresh_from_db()
        return context


def ajax_like(request):
    if request.POST:
        picture = Picture.objects.get(slug=request.POST.get('slug'))
        picture.rate = F('rate') + 1
        picture.save()
        picture.refresh_from_db()
        return JsonResponse({'like': picture.rate})
    else:
        return redirect('/')
