from product.models import Category
from page.models import Page

def nav_data(request):
    context = dict()
    context['categories'] = Category.objects.filter(
        status='published'
    )
    context['pages'] = Page.objects.filter(
        status='published'
    )
    return context
