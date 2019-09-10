from django.shortcuts import render, get_object_or_404
from .models import Category, Product


def category_show(request, category_slug):
    context = dict()
    context['category'] = get_object_or_404(Category, slug=category_slug)
    # context['categories'] = Category.objects.filter(
    #     status='published',
    # )
    context['items'] = Product.objects.filter(
        status='published',
        stock__gte=1,
        category=context['category'],
    )
    return render(request, 'product/category_show.html', context)
