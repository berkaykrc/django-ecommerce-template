from django.db import models
from page.models import DEFAULT_STATUS, STATUS


GENDER_CHOICE = [
    ('man', "Erkek"),
    ('women', 'Kadin'),
    ('unisex', 'Unisex')
]

class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(
        max_length=75,
    )
    created_at = models.DateTimeField()
    status = models.CharField(
        choices=STATUS,
        max_length=10,
        default=DEFAULT_STATUS,
    )
    gender = models.CharField(
        default='unisex',
        max_length=6,
        choices=GENDER_CHOICE,
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
            return self.title


class Product(models.Model):
    category = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        null=True,
    )
    title = models.CharField(max_length=50)
    slug = models.SlugField(
        max_length=200,
        default="",
    )
    content = models.TextField()
    cover_image = models.ImageField(
        upload_to='product',
        null=True,
        blank=True,
    )
    stock = models.PositiveSmallIntegerField(default=0)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    status = models.CharField(
        choices=STATUS,
        max_length=10,
        default=DEFAULT_STATUS,
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )
