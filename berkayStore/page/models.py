from django.db import models

STATUS = [
    ('draft', "Taslak"),
    ('published', "Yayinlandi"),
    ('deleted', "Silindi"),
]


class Page(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    cover_image = models.ImageField(upload_to="page")
    # slug =
    status = models.CharField(
        choices=STATUS,
        max_length=10,
        default='draft',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
