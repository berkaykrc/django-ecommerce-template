from django.urls import path
from .views import (
    # manage
    manage_list,
    # carousel
    carousel_create,
    carousel_list,
    carousel_update,
    # page
    page_view,
    page_list,
    page_create,
    page_update,
)
urlpatterns = [
    path('', manage_list, name='manage_list'),
    path(
        'carousel/list/',
        carousel_list,
        name='carousel_list'
    ),
    path('carousel/create/', carousel_create, name='carousel_create'),
    path(
        'carousel/update/<int:pk>/',
        carousel_update,
        name='carousel_update'
    ),
    path('page/list/', page_list, name='page_list'),
    path('page/create/', page_create, name='page_create'),
    path('page/update/<int:pk>/', page_update, name='page_update'),
    path('page/<slug:slug>/', page_view, name='page_view'),
]
