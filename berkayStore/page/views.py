from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)

from django.utils.text import slugify
from .models import Carousel, Page
from django.contrib import messages
from .forms import CarouselModelForm, PageModelForm
from product.models import Category, Product


def index(request): 
    context = dict()
    context['images'] = Carousel.objects.filter(
        status='published'
    ).exclude(cover_image='')
    context['products'] = Product.objects.filter(
        in_homepage=True,
    )

    return render(request, 'home/index.html', context)


def page_view(request, slug):
    context = dict()
    context['page'] = get_object_or_404(Page, slug=slug)
    return render(request, 'page/page.html', context)


def manage_list(request):
    context = dict()
    return render(request, 'manage/manage.html', context)


def page_list(request):
    context = dict()
    context['items'] = Page.objects.all()
    return render(request, 'manage/page_list.html', context)


def page_create(request):
    context = dict()
    context['form'] = PageModelForm()
    context['title'] = 'Page Create Form'
    if request.method == 'POST':
        form = PageModelForm(request.POST, request.FILES)
        if form.is_valid():
            new_page = form.save(commit=False)
            new_page.slug = slugify(item.title.replace('ı', 'i'))
            new_page.save()
            messages.success(request, 'Sayfanız eklendi')
    return render(request, 'manage/create_form.html', context)


def page_update(request, pk):
    context = dict()
    item = Page.objects.get(pk=pk)
    context['form'] = PageModelForm(instance=item)
    context['title'] = f'{item.title} Update'
    if request.method == 'POST':
        form = PageModelForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            if not item.slug:
                item.slug = slugify(item.title.replace('ı', 'i'))
            form.save()
            return redirect('page_update', pk)
    return render(request, 'manage/create_form.html', context)


def carousel_create(request):
    context = dict()
    context['form'] = CarouselModelForm()
    context['title'] = 'Carousel Create'
    if request.method == 'POST':
        print(request.POST)
        print(request.FILES.get('cover_image'))
        form = CarouselModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        messages.success(request, 'Anasayfaya slider eklendi')
    return render(request, 'manage/create_form.html', context)


def carousel_list(request):
    context = dict()
    context['carousel'] = Carousel.objects.all()
    return render(request, 'manage/carousel_list.html', context)


def carousel_update(request, pk):
    context = dict()
    item = Carousel.objects.get(pk=pk)
    context['form'] = CarouselModelForm(instance=item)
    context['title'] = f'{item.title} Update'
    if request.method == 'POST':
        form = CarouselModelForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('carousel_update', pk)
    return render(request, 'manage/create_form.html', context)
