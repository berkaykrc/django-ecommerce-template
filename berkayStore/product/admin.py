from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = (
        "pk",
        "title",
        "price",
        "stock",
        "cover_image",
        "status",
        "updated_at",
        "created_at",
    )
    list_filter = (
        "status",
        "price",
    )

    list_editable = (
        "title",
        "status",
    )


class CategoryAdmin(admin.ModelAdmin):

    prepopulated_fields = {"slug": ("title",)}
    list_display = (
        "pk",
        "title",
        "gender",
        "slug",
        "status",
        "updated_at",
        "created_at",
    )
    list_filter = (
        "status",
        "gender",
    )

    list_editable = (
        "title",
        "status",
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
