from django.shortcuts import render
from .models import Carousel


def index(request):
    context = dict()
    context['images'] = Carousel.objects.filter(status="published")
    return render(request, 'home/index.html', context)
