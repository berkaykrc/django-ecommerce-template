from django.db import models

DEFATULT_STATUS = 'draft'

STATUS = [
    ('draft', "Taslak"),
    ('published', "Yayinlandi"),
    ('deleted', "Silindi"),
]


class Page(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    cover_image = models.ImageField(
        upload_to="page",
        null=True,
        blank=True,
    )
    slug = models.SlugField(
        max_length=200,
        default="",
    )
    status = models.CharField(
        choices=STATUS,
        max_length=10,
        default=DEFATULT_STATUS,
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )


class Carousel(models.Model):
    title = models.CharField(
        max_length=100,
        null=True,
        blank=True,
    )
    cover_image = models.ImageField(
        upload_to="carousel"
    )
    status = models.CharField(
        max_length=10,
        choices=STATUS,
        default=DEFATULT_STATUS,
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )
