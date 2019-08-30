from django.shortcuts import render,redirect
from .models import Carousel
from django.contrib import messages
from .forms import CarouselModelForm


def index(request):
    context = dict()
    context['images'] = Carousel.objects.filter(
        status='published',
    ).exclude(cover_image='')
    return render(request, 'home/index.html', context)

def manage_list(request):
    context = dict()
    return render(request, 'manage/manage.html', context)


def carousel_create(request):
    context = dict()
    context['form'] = CarouselModelForm()
    if request.method == 'POST':
        print(request.POST)
        print(request.FILES.get('cover_image'))
        form = CarouselModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        messages.success(request, 'Birseyler eklendi ama ne oldu bilemiyorum')
    return render(request, 'manage/carousel_form.html', context)

def carousel_list(request):
    context = dict()
    context['carousel'] = Carousel.objects.all()
    return  render(request, 'manage/carousel_list.html', context)


def carousel_update(request, pk):
    context = dict()
    item = Carousel.objects.get(pk=pk)
    context['form'] = CarouselModelForm(instance=item)
    if request.method == 'POST':
        form = CarouselModelForm(request.POST, request.FILES, instance= item)
        if form.is_valid():
            form.save()
            return redirect('carousel_update', pk)
    return render(request, 'manage/carousel_form.html', context)
